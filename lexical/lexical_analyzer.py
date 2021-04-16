from dfa_tables import ARITHMETIC_OPERATOR,COMPARISON_1,COMPARISON_2,COMPARISON_3,COMPARISON_4,COMPARISON_5,SIGN_INTEGER,ID,BRACE,ZERO,LITERAL_STRING,SINGLE_CHARACTER,PAREN,BRACKET,WHITESPACE,SEPARATE,SEMI,ASSIGN,BOOL,VARIABLE_TYPE,KEYWORD,DDAOM_ERROR


class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.tableName = ""

    # dfa table을 가져오는 함수
    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates=_dfa["AcceptedStates"]
        self.tableName =_dfa["Name"]

    # table name을 return하는 함수  
    def GetTableName(self):
        return self.tableName
 
     # table name을 return하는 함수
    def PeekNextState(self, _input, _origin_digit=None): 
        # table에 input 들어가기전에 input 형태 변경해주기     
        if _input.isalpha() and self.GetTableName()=='ID' :
            _input='LETTER'

        elif _input.isalpha() and self.GetTableName()=='SINGLE_CHARACTER' :
           _input='LETTER'     

        elif _input.isalpha() and self.GetTableName()=='LITERAL_STRING' :
            _input='LETTER' 
        
        elif _input.isdigit():
            if _input != '0':
                _input='EXCEPT_ZERO'

        # 현재 상태에 해당하는 table이 없을 경우
        if not self.currentState in self.table:
            return "Error"
        else :
            # input에 해당하는 state가 없을 경우
            if not _input in self.table[self.currentState]:
                return "Error"
        
        nextState = self.table[self.currentState][_input]

        if nextState == "":
            return "Rejected"

        else:
            return nextState

    # 현재 state를 return하는 함수
    def GetState(self):
        return self.currentState
 
    # 현재 state를 해당 state로 설정하는 함수
    def SetState(self, _state):
        self.currentState = _state

    # accept된 state를 반환하고, accept되지 않았을 경우 error를 return하는 함수
    def GetToken(self):
        if self.currentState in self.acceptedStates:
            return self.acceptedStates[self.currentState]
        else:
            return "Error"
 
    # accept 되었을 경우 true를, 그렇지 않을 경우 false를 return하는 함수
    def IsAccepted(self):
        if self.currentState in self.acceptedStates:
            return True
        else:
            return False

    # 해당 state가 accept 되었을 경우 true를, 그렇지 않을 경우 false를 return하는 함수
    def temp_IsAccepted(self,temp_currentState):
        if temp_currentState in self.acceptedStates:
            return True
        else:
            return False
    # 초기화해주는 함수
    def Reset(self):
        self.currentState = "T0"
 
# error가 발생했을 때의 출력
def print_error_text(input_char, filename,error_line):
    error_text=["Error : ",input_char," is unknown symbol(s)\n",'    File "',filename,'", line_number ',str(error_line)]
    return error_text

if __name__=="__main__":
    filename = input()
    # input 파일
    f = open("./lexical/"+filename, 'r')
    # 한줄씩 읽어줌
    readlines = f.readlines()
    lines=[]
    for line in readlines:
        if line.find('\n') != -1 :
            line=line[:-1]
        # line=line+" "
        lines.append(line+" ")
    f.close()

    # output파일
    out_f = open("./lexical/"+filename[:-4]+".out.txt", 'w')

    error_line=0

    # 우선순위 순으로 포함시켜야함 ! 
    transition_table_1=[ARITHMETIC_OPERATOR,SIGN_INTEGER,SINGLE_CHARACTER,LITERAL_STRING,DDAOM_ERROR,ID,BRACE,PAREN,BRACKET,ZERO,COMPARISON_3,COMPARISON_2,COMPARISON_4,COMPARISON_5,COMPARISON_1,WHITESPACE,SEPARATE,SEMI,ASSIGN]
    transition_table_2=[BOOL,VARIABLE_TYPE,KEYWORD]

    dfa = FiniteAutomaton()

    temp_input_char = []
    temp_getTableName = ""
    state = []

    for line_number, inputString in enumerate(lines):
        for index, input_char in enumerate(inputString) :
            for i in range(0,len(transition_table_1)):
                dfa.LoadTransitionTable(transition_table_1[i])
                if temp_getTableName != "": 
                    # input이 숫자일 경우 DIGIT으로 설정
                    if input_char.isdigit():
                        input_char="DIGIT"                
                    if dfa.GetTableName()==temp_getTableName:
                        nextState = dfa.PeekNextState(input_char)
                        dfa.SetState(nextState)

                        if dfa.IsAccepted():
                            next_index=index+1
                            try:
                                next_input_char = inputString[next_index]
                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"

                                next_input_state = dfa.PeekNextState(next_input_char)

                                # 원래 input 값 origin_input_char 변수에 두기
                                if input_char=='DIGIT':
                                        origin_input_char=inputString[index]
                                else :
                                    origin_input_char=input_char

                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    temp_input_char.append(origin_input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break
                                else:
                                    temp_input_char.append(origin_input_char)
                                    str_temp_input_char=''.join(temp_input_char)

                                    if dfa.GetTableName() == 'ID':
                                        change_dfa = FiniteAutomaton()
                                        is_identifier=0
                                        for i in range(0,len(transition_table_2)):
                                            change_dfa.LoadTransitionTable(transition_table_2[i])
                                            
                                            if change_dfa.PeekNextState(str_temp_input_char)=="Error" :
                                                is_identifier=is_identifier+1
                                                if is_identifier==3:
                                                    data="<"+dfa.GetToken()+","+str_temp_input_char+">, "
                                                    out_f.write(data)
                                                    state.append(dfa.GetToken())
                                                else:
                                                    continue
                                            else :
                                                nextState = change_dfa.PeekNextState(str_temp_input_char)
                                                change_dfa.SetState(nextState)
                                                if change_dfa.IsAccepted():
                                                    data="<"+change_dfa.GetToken()+","+str_temp_input_char+">, "
                                                    out_f.write(data)
                                                    state.append(change_dfa.GetToken())
                                                    break 
                                        change_dfa.Reset()
                                    else :
                                        data="<"+dfa.GetToken()+","+str_temp_input_char+">, "
                                        if dfa.GetToken()=='Error':
                                            out_f.close()
                                            # open("./lexical/"+filename+"_out.txt", 'w')
                                            with open("./lexical/"+filename+"_out.txt", 'w') as error_f:
                                                error_line=line_number+1
                                                error_f.writelines(print_error_text(str_temp_input_char,filename,error_line))
                                            exit()
                                        else :
                                            out_f.write(data)
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

                                next_input_state = dfa.PeekNextState(next_input_char)

                                # 원래 input 값 origin_input_char 변수에 두기
                                if input_char=='DIGIT':
                                        origin_input_char=inputString[index]
                                else :
                                    origin_input_char=input_char

                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    temp_input_char.append(origin_input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break
                                else:
                                    temp_input_char.append(origin_input_char)
                                    str_temp_input_char=''.join(temp_input_char)
                                    data="<"+dfa.GetToken()+","+str_temp_input_char+">, "
                                    if dfa.GetToken()=='Error':
                                        out_f.close()
                                        # open("./lexical/"+filename+"_out.txt", 'w')
                                        with open("./lexical/"+filename+"_out.txt", 'w') as error_f:
                                            error_line=line_number+1
                                            error_f.writelines(print_error_text(str_temp_input_char,filename,error_line))
                                        exit()
                                    else :
                                        out_f.write(data)
                                        state.append(dfa.GetToken())
                                    
                                    temp_input_char = [] #초기화
                                    temp_getTableName = "" #초기화
                                    dfa.Reset()
                                    break
                            except IndexError :
                                # !! 
                                pass

                    else:
                        continue

                else :

                    if dfa.PeekNextState(input_char)=="Error" :
                        if input_char == '"':
                                next_index=index+1
                                next_input_char = inputString[next_index]
                                if(next_input_char=='"'):
                                    temp_input_char.append(input_char)
                                    temp_getTableName = "DDAOM_ERROR"
                                    break                                            
                        if i == len(transition_table_1)-1:
                            if input_char=='<':
                                data="<"+"COMPARISON"+","+input_char+">, "
                                out_f.write(data)
                            else :
                                data="<"+dfa.GetToken()+","+input_char+">, "
                                if dfa.GetToken()=='Error':
                                    out_f.close()
                                    with open("./lexical/"+filename+"_out.txt", 'w') as error_f:
                                        error_line=line_number+1
                                        error_f.writelines(print_error_text(input_char,filename,error_line))
                                    exit()
                                else :
                                    out_f.write(data)
                                    state.append(dfa.GetToken())
                        dfa.Reset()

                    else :
                        nextState = dfa.PeekNextState(input_char)
                        dfa.SetState(nextState)
                        if dfa.IsAccepted():
                            try:                                                 
                                next_index=index+1
                                next_input_char = inputString[next_index]

                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"
                                next_input_state = dfa.PeekNextState(next_input_char)
                                
                                # symbol - 처리
                                if input_char=="-":
                                    pos = index
                                    next_index=index+1
                                    next_input_char = inputString[next_index]
                                
                                # - 뒤 숫자가 올 경우
                                    if next_input_char.isdigit():
                                        pos = len(state) 
                                        # -가 맨 첫번째로 올 경우 음수로 처리
                                        if pos == 0:
                                            temp_input_char.append(input_char)
                                            temp_getTableName = "SIGN_INTEGER"
                                            break
                                        # 다음 input이 0이거나, 전 input이 숫자거나 identifier일 때에만 OP로 처리
                                        elif (state[pos-1] == "ID" or state[pos-1] == "INTEGER" or state[pos-1] == "CHAR" or next_input_char== '0') :
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
                                if next_input_state != 'Error' and next_input_state != 'Rejected':
                                    temp_input_char.append(input_char)
                                    temp_getTableName = dfa.GetTableName()
                                    break                        
                                else:
                                    if dfa.GetToken()=="WHITESPACE":
                                        dfa.Reset()
                                        break                              
                                    else :
                                        state.append(dfa.GetToken())                     
                                        data="<"+dfa.GetToken()+","+input_char+">, "
                                        out_f.write(data)
                                        dfa.Reset()
                                        break
                            except IndexError:
                                if dfa.GetToken()=="WHITESPACE":
                                        dfa.Reset()
                                        break
                                else:
                                    data="<"+dfa.GetToken()+","+input_char+">, "
                                    out_f.write(data)
                                    state.append(dfa.GetToken())
                                    dfa.Reset()
                        
                        else:
                            #single_character이랑 literal_string 부분이 여기로 들어옴
                            try:
                                next_index=index+1
                                next_input_char = inputString[next_index]
                                if next_input_char.isdigit():
                                    next_input_char="DIGIT"

                                next_input_state = dfa.PeekNextState(next_input_char)

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
        out_f.write('\n')
    out_f.close()
    print("성공적으로 출력파일이 생성되었습니다.")