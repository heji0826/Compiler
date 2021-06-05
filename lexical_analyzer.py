from dfa_tables import ARITHMETIC_OPERATOR,COMPARISON_1,COMPARISON_2,COMPARISON_3,COMPARISON_4,COMPARISON_5,SIGN_INTEGER,ID,BRACE,ZERO,LITERAL_STRING,SINGLE_CHARACTER,PAREN,BRACKET,WHITESPACE,SEPARATE,SEMI,ASSIGN,BOOL,VARIABLE_TYPE,KEYWORD,DDAOM_ERROR
import sys

# error가 발생했을 때, output파일의 텍스트 출력해주는 함수
def print_error_text(input_char, filename,error_line):
    error_text=["Error : ",input_char," is unknown symbol(s)\n",'    File "',filename,'", line_number ',str(error_line)]
    return error_text

class DFAautomata:
    # 가져올 transition 테이블, 테이블이름, 현재상태, aceept한 상태들에 대한 변수 선언
    def __init__(self):
        self.tableName = ""
        self.table = {}
        self.crr_T = "T0"
        self.acceptTN = {}
        
    # table name을 return하는 함수  
    def GetTableName(self):
        return self.tableName

    # dfa table을 가져오는 함수
    def GetTable(self, dfa):
        self.table = dfa["Table"]
        self.acceptTN=dfa["AcceptTN"]
        self.tableName =dfa["Name"]

    # 입력된 input을 기준으로 다음 상태를 확인해주는 함수 
    def CheckNextState(self, input, _origin_digit=None): 
        # table에 input 들어가기전에 input 형태 변경해주기     
        if input.isalpha() and self.GetTableName()=='ID' :
            input='LETTER'

        elif input.isalpha() and self.GetTableName()=='SINGLE_CHARACTER' :
           input='LETTER'     

        elif input.isalpha() and self.GetTableName()=='LITERAL_STRING' :
            input='LETTER' 
        
        elif input.isdigit():
            if input != '0':
                input='EXCEPT_ZERO'

        # 현재 상태에 해당하는 table이 없을 경우
        if not self.crr_T in self.table:
            return "Error"
        else :
            # input에 해당하는 state가 없을 경우
            if not input in self.table[self.crr_T]:
                return "Error"
        
        nextState = self.table[self.crr_T][input]

        # 현재상태에서 유효한 input이 더이상 없는 경우
        if nextState == "":
            return "Rejected"
        
        else:
            return nextState

    # 현재 state를 해당 state로 설정하는 함수
    def SetState(self, state):
        self.crr_T = state

    # accept된 state를 반환하고, accept되지 않았을 경우 error를 return하는 함수
    def GetToken(self):
        if self.crr_T in self.acceptTN:
            return self.acceptTN[self.crr_T]
        else:
            return "Error"
 
    # accept 되었을 경우 true를, 그렇지 않을 경우 false를 return하는 함수
    def IsAccepted(self):
        if self.crr_T in self.acceptTN:
            return True
        else:
            return False

    # 초기화해주는 함수
    def Reset(self):
        self.crr_T  = "T0"
 


if __name__=="__main__":
    # filename = input()
    filename = sys.argv[-1]
    # input 파일
    f = open(filename, 'r')
    # 라인별로 한줄씩 읽어줌
    readlines = f.readlines()
    lines=[]
    for line in readlines:
        if line.find('\n') != -1 :
            line=line[:-1]
        # line=line+" "
        lines.append(line+" ")
    f.close()

    # output파일
    out_f = open("./"+filename[:-4]+".out.txt", 'w')

    # error 발생시 해당 error의 코드라인을 저장해주는 변수
    error_line=0

    # 하드코딩한 transition_table을 리스트에 저장 ( 우선순위를 고려하여 그 순서대로 저장 )
    transition_table_1=[ARITHMETIC_OPERATOR,SIGN_INTEGER,SINGLE_CHARACTER,LITERAL_STRING,DDAOM_ERROR,ID,BRACE,PAREN,BRACKET,ZERO,COMPARISON_3,COMPARISON_2,COMPARISON_4,COMPARISON_5,COMPARISON_1,WHITESPACE,SEPARATE,SEMI,ASSIGN]
    transition_table_2=[BOOL,VARIABLE_TYPE,KEYWORD]

    # dfa 객체 생성
    dfa = DFAautomata()

    # input이 단순 단일문자가 아닌경우 ( *같은 input이 아닌 abc처럼 다음 문자도 봐야할 경우 ) 현 input을 임시 저장해놓는 temp변수들
    temp_input_char = []
    temp_getTableName = ""
    state = []

    # 삼중 for문 : 입력파일 line별 읽기 -> 각 line별 input_char 읽기 -> transition table 순회하기

    for line_number, inputString in enumerate(lines):
        for index, input_char in enumerate(inputString) :
            for i in range(0,len(transition_table_1)):
                dfa.GetTable(transition_table_1[i])

                # temp변수들에 값이 들어가 있는경우 (이전문자들에 이어서 상태들을 확인해야하는 모든 경우)
                if temp_getTableName != "": 
                    # input이 숫자일 경우 DIGIT으로 설정
                    if input_char.isdigit():
                        input_char="DIGIT"      
                    
                    # 이전 문자들에 이어 상태를 확인해햐하기 때문에 이전문자와 동일한 테이블을 가지고 처리해야함
                    if dfa.GetTableName()==temp_getTableName: # temp_getTableName과 현재 가져온 테이블이 같을때에만 처리
                        nextState = dfa.CheckNextState(input_char)
                        dfa.SetState(nextState)

                        if dfa.IsAccepted():
                            next_index=index+1
                            try:
                                next_input_char = inputString[next_index]
                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"

                                next_input_state = dfa.CheckNextState(next_input_char)

                                # 원래 input 값은 origin_input_char 변수에 두기
                                if input_char=='DIGIT':
                                        origin_input_char=inputString[index]
                                else :
                                    origin_input_char=input_char

                                # 다음 문자도 unknown심볼이 아니고 동시에 이동할 상태가 남아있는 경우
                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    # temp 변수들에 현재 input과 테이블 이름 계속 추가
                                    temp_input_char.append(origin_input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break
                                else:
                                    # 다음문자에서부터는 reject라면 지금 input문자까지 temp변수에 저장한 후 이를 출력해준다.
                                    temp_input_char.append(origin_input_char)
                                    str_temp_input_char=''.join(temp_input_char)
                                    
                                    # 테이블이름이 ID인 경우 
                                    # 본 팀은 우선순위를 주는 방법을 먼저 ID로 분류된 것들 중 
                                    # transition_table_2에 해당하는 [BOOL,VARIABLE_TYPE,KEYWORD] input이면 이것으로 바꿔주도록 구현했다
                                    # 결국에 우선순위는 BOOL,VARIABLE_TYPE,KEYWORD > IDENTIFIER가  된다.
                                    if dfa.GetTableName() == 'ID':
                                        change_dfa = DFAautomata()
                                        is_identifier=0

                                        # transition_table_2에서 accept되는 input들이 있는지 검사하는 for문
                                        for i in range(0,len(transition_table_2)):
                                            change_dfa.GetTable(transition_table_2[i])
                                            
                                            if change_dfa.CheckNextState(str_temp_input_char)=="Error" :
                                                is_identifier=is_identifier+1
                                                if is_identifier==3:
                                                    data=dfa.GetToken()
                                                    out_f.write(data+" ")
                                                    state.append(dfa.GetToken())
                                                else:
                                                    continue
                                            else :
                                                nextState = change_dfa.CheckNextState(str_temp_input_char)
                                                change_dfa.SetState(nextState)
                                                if change_dfa.IsAccepted():
                                                    data=change_dfa.GetToken()
                                                    out_f.write(data+" ")
                                                    state.append(change_dfa.GetToken())
                                                    break 
                                        change_dfa.Reset()
                                    else :
                                        data=dfa.GetToken()
                                        if dfa.GetToken()=='Error':
                                            out_f.close()
                                            with open("./lexical/"+filename[:-4]+".out.txt", 'w') as error_f:
                                                error_line=line_number+1
                                                error_f.writelines(print_error_text(str_temp_input_char,filename,error_line))
                                            exit()
                                        else :
                                            out_f.write(data+" ")
                                            state.append(dfa.GetToken())

                                    temp_input_char = [] #초기화
                                    temp_getTableName = "" #초기화
                                    dfa.Reset()
                                    break
                            except IndexError:
                                pass
                        else :
                            # single character이나 literal 아직 끝마무리 안되었을때
                            next_index=index+1
                            try :
                                next_input_char = inputString[next_index]

                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"

                                next_input_state = dfa.CheckNextState(next_input_char)

                                # 원래 input 값 origin_input_char 변수에 두기
                                if input_char=='DIGIT':
                                        origin_input_char=inputString[index]
                                else :
                                    origin_input_char=input_char

                                # 다음 문자도 unknown심볼이 아니고 동시에 이동할 상태가 남아있는 경우
                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    # 계속 temp변수들에 저장
                                    temp_input_char.append(origin_input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break
                                # 다음 문자에 대한 상태가 reject이면 현 input문자만 temp변수에 저장하고 이를 출력해준다.
                                else:
                                    temp_input_char.append(origin_input_char)
                                    str_temp_input_char=''.join(temp_input_char)
                                    data=dfa.GetToken()
                                    # error인경우에 대한 핸들링
                                    if dfa.GetToken()=='Error':
                                        out_f.close()
                                        # 작성하던 output 파일을 다시 열어 (초기화행위) error_report를 출력시켜줌
                                        with open("./lexical/"+filename[:-4]+".out.txt", 'w') as error_f:
                                            error_line=line_number+1
                                            error_f.writelines(print_error_text(str_temp_input_char,filename,error_line))
                                        exit()
                                    else :
                                        out_f.write(data+" ")
                                        state.append(dfa.GetToken())
                                    
                                    temp_input_char = [] #초기화
                                    temp_getTableName = "" #초기화
                                    dfa.Reset()
                                    break
                            except IndexError :
                                pass
                    else:
                        continue
                
                # 이전문자를 고려할 필요가 없는 경우 (temp변수들이 다 None인 경우)
                else :
                    # 정의하지 않은 input이 들어왔을 때
                    if dfa.CheckNextState(input_char)=="Error" :
                        if input_char == '"':
                                next_index=index+1
                                next_input_char = inputString[next_index]
                                if(next_input_char=='"'):
                                    temp_input_char.append(input_char)
                                    temp_getTableName = "DDAOM_ERROR"
                                    break                                            
                        if i == len(transition_table_1)-1:
                            if input_char=='<':
                                data="comp"
                                out_f.write(data+" ")
                            else :
                                data=dfa.GetToken()
                                # error인경우
                                if dfa.GetToken()=='Error':
                                    out_f.close()
                                    # 작성하던 output 파일을 다시 열어 (초기화행위) error_report를 출력시켜줌
                                    with open("./lexical/"+filename[:-4]+".out.txt", 'w') as error_f:
                                        error_line=line_number+1 # 에러난 코드의 라인넘버 확인 및 저장
                                        error_f.writelines(print_error_text(input_char,filename,error_line))
                                    exit()
                                else :
                                    out_f.write(data+" ")
                                    state.append(dfa.GetToken())
                        # 다음 table 확인을 위해 reset후 for문 진행
                        dfa.Reset()

                    else :
                        nextState = dfa.CheckNextState(input_char)
                        dfa.SetState(nextState)
                        # 현 상태가 accept일때
                        if dfa.IsAccepted():
                            # 다음 input이 들어와도 accept한 상태인지 확인하는 일련의 과정
                            try:                                                 
                                next_index=index+1
                                next_input_char = inputString[next_index]
                                
                                # 숫자면 일괄적으로 DIGIT로 문자의 이름을 재정의해준다
                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"
                                next_input_state = dfa.CheckNextState(next_input_char)
                                
                                # symbol - 처리
                                if input_char=="-":
                                    pos = index
                                    next_index=index+1
                                    next_input_char = inputString[next_index]
                                    
                                # - 뒤 숫자가 올 경우
                                    if next_input_char.isdigit():
                                        pos = len(state) 
                                        # 다음 input이 0일 경우
                                        if next_input_char== '0':
                                            pass
                                        # -가 맨 첫번째로 올 경우 음수로 처리
                                        elif pos == 0:
                                            temp_input_char.append(input_char)
                                            temp_getTableName = "SIGN_INTEGER"
                                            break
                                        # 전 input이 숫자거나 identifier이거나 char일 때에만 OP로 처리
                                        elif (state[pos-1] == "ID" or state[pos-1] == "INTEGER" or state[pos-1] == "CHAR") :
                                            pass
                                        # 나머지의 경우 음수로 처리
                                        else:
                                            temp_input_char.append(input_char)
                                            temp_getTableName = "SIGN_INTEGER"
                                            break  
                                # = 기호 뒤에 = 가 나올 경우에 comparison으로 처리                                                                         
                                if input_char=="=":
                                    if next_input_char == "=":
                                            temp_input_char.append(input_char)
                                            temp_getTableName = "COMPARISON_2"
                                            break 
                                    # = 기호 뒤에 = 가 없는 경우 assign으로 처리
                                    else:
                                        pass  
                                # 다음 input의 상태도 accept일경우
                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    # 다음 input에서 진행할때 현재 input이 무엇인지 저장해두어야하기 떄문에 이러한 상황에서
                                    # temp변수들에 값들을 임시로 저장해둔다.
                                    temp_input_char.append(input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break                        
                                else:
                                    # WHITESPACE는 무시한다. 고로 출력하지 않는다.
                                    if dfa.GetToken()=="WHITESPACE":
                                        dfa.Reset()
                                        break       
                                    # 다음 input의 상태가 reject이면 바로 현 토큰이름과 현재 input을 출력해준다.                      
                                    else :
                                        state.append(dfa.GetToken())                     
                                        data=dfa.GetToken()
                                        out_f.write(data+" ")
                                        dfa.Reset()
                                        break
                            # 예외처리 : 입력파일의 가장 마지막 문자에 대한 핸들링 부분
                            except IndexError:
                                if dfa.GetToken()=="WHITESPACE":
                                        dfa.Reset()
                                        break
                                else:
                                    data=dfa.GetToken()
                                    out_f.write(data+" ")
                                    state.append(dfa.GetToken())
                                    dfa.Reset()
                        
                        # 현재 accept가 아니지만 다음 문자에 대한 state를 확인했을때 갈 수 있는 상태가 또 있는 경우 
                        #single_character이랑 literal_string 부분이 여기로 들어옴
                        else:
                            try:
                                next_index=index+1
                                next_input_char = inputString[next_index]
                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"

                                next_input_state = dfa.CheckNextState(next_input_char)

                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    temp_input_char.append(input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break

                            except IndexError:
                                if dfa.GetToken()=="WHITESPACE":
                                        dfa.Reset()
                                        break
                                else:
                                    pass
        # out_f.write('\n')
    out_f.close()
    print("성공적으로 출력파일이 생성되었습니다.")