from dfa_tables import ARITHMETIC_OPERATOR,SIGN_INTEGER,IDENTIFIER,BRACE,ZERO,LITERAL_STRING,SINGLE_CHARACTER,PAREN,BRACKET,WHITESPACE,SEPARATE,SEMI,ASSIGN,BOOL_STRING,VARIABLE_TYPE,KEYWORD

def handling_integer():
    # temp에 넣어진 값과, 현재 진행중인 그 토큰 이름을 파라미터로 받아서
    # 이게 zero인지,, 사실 제로면 바로 끝내야함
    # 아니면 except_zero인지,,, digit인지 확인해서 .. 바로 peekNextState에 넣어버리자!
    pass


class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.tableName = ""

    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates=_dfa["AcceptedStates"]
        self.tableName =_dfa["Name"]

    def GetTableName(self):
        return self.tableName
 
    def PeekNextState(self, _input): 
        # table에 input 들어가기전에 input 형태 변경해주기     
        if _input.isalpha() and self.GetTableName()=='IDENTIFIER' :
            _input='LETTER'

        elif _input.isalpha() and self.GetTableName()=='SINGLE_CHARACTER' :
           _input='LETTER'

        elif _input.isalpha() and self.GetTableName()=='LITERAL_STRING' :
            _input='LETTER' 


        # 현재 T4인데 첫 transition에 애초에 T4가 없는경우엔 바로 빠져나가야해
        if not self.currentState in self.table:
            return "Unknown"
        else :
            if not _input in self.table[self.currentState]:
                return "Unknown"
        
        nextState = self.table[self.currentState][_input]

        if nextState == "":
            return "Rejected"

        else:
            return nextState
    
    def GetState(self):
        return self.currentState
 
    def SetState(self, _state):
        self.currentState = _state
 
    def GetToken(self):
        if self.currentState in self.acceptedStates:
            return self.acceptedStates[self.currentState]
        else:
            return "Unknown Token"
 
    def IsAccepted(self):
        if self.currentState in self.acceptedStates:
            return True
        else:
            return False

    def temp_IsAccepted(self,temp_currentState):
        if temp_currentState in self.acceptedStates:
            return True
        else:
            return False
 
    def Reset(self):
        self.currentState = "T0"
 

if __name__=="__main__":
    f = open("./lexical/input.txt", 'r')
    inputString = f.read()
    f.close()
    # 우선순위 순으로 포함시켜야함 ! 
    transition_table_1=[ARITHMETIC_OPERATOR,SIGN_INTEGER,IDENTIFIER,BRACE,PAREN,BRACKET,ZERO,WHITESPACE,SEPARATE,SEMI,ASSIGN]
    # ,LITERAL_STRING,SINGLE_CHARACTER
    # COMPARISON
    transition_table_2=[BOOL_STRING,VARIABLE_TYPE,KEYWORD]

    dfa = FiniteAutomaton()

    temp_input_char = []
    temp_getTableName = ""

    for index, input_char in enumerate(inputString) :
        for i in range(0,len(transition_table_1)):
            dfa.LoadTransitionTable(transition_table_1[i])

            if temp_getTableName != "":
                
                if dfa.GetTableName()==temp_getTableName:
                   
                    nextState = dfa.PeekNextState(input_char)
                    dfa.SetState(nextState)

                    if dfa.IsAccepted():
                        next_index=index+1
                        next_input_state = dfa.PeekNextState(inputString[next_index])

                        if next_input_state != 'Unknown' and next_input_state != 'Rejected':
                            temp_input_char.append(input_char)
                            temp_getTableName = dfa.GetTableName()
                            break
                        else:
                            temp_input_char.append(input_char)
                            str_temp_input_char=''.join(temp_input_char)

                            if dfa.GetTableName() == 'IDENTIFIER':
                                change_dfa = FiniteAutomaton()
                                is_identifier=0
                                for i in range(0,len(transition_table_2)):
                                    change_dfa.LoadTransitionTable(transition_table_2[i])
                                    
                                    if change_dfa.PeekNextState(str_temp_input_char)=="Unknown" :
                                        is_identifier=is_identifier+1
                                        if is_identifier==3:
                                            print("<",dfa.GetToken(),",",str_temp_input_char,">,")
                                        else:
                                            continue
                                    else :
                                        nextState = change_dfa.PeekNextState(str_temp_input_char)
                                        change_dfa.SetState(nextState)
                                        if change_dfa.IsAccepted():
                                            print("<",change_dfa.GetToken(),",",str_temp_input_char,">,")
                                            break 
                            else :
                                print("<",dfa.GetToken(),",",str_temp_input_char,">,")
                            
                            temp_input_char = [] #초기화
                            temp_getTableName = "" #초기화
                            change_dfa.Reset()
                            dfa.Reset()
                            break
                else:
                    #if123같은 것들이 들어오는 경우에 해당하는 조건
                    continue

            else :
                
                if dfa.PeekNextState(input_char)=="Unknown" :
                    dfa.Reset()

                else :
                    
                    nextState = dfa.PeekNextState(input_char)
                    dfa.SetState(nextState)

                    if dfa.IsAccepted():
                        next_index=index+1
                        
                        try:
                            next_input_state = dfa.PeekNextState(inputString[next_index])
                            if next_input_state != 'Unknown' and next_input_state != 'Rejected':
                                temp_input_char.append(input_char)
                                temp_getTableName = dfa.GetTableName()
                                break
                            else:
                                if dfa.GetToken()=="WHITESPACE":
                                    dfa.Reset()
                                    break
                                else :
                                    print("<",dfa.GetToken(),",",input_char,">,")
                                    dfa.Reset()
                                    break
                        except IndexError:
                            if dfa.GetToken()=="WHITESPACE":
                                    dfa.Reset()
                                    break
                            else:
                                print("<",dfa.GetToken(),",",input_char,">,")
