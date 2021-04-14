from dfa_tables import ARITHMETIC_OPERATOR,COMPARISON_1,COMPARISON_2,COMPARISON_3,COMPARISON_4,COMPARISON_5,SIGN_INTEGER,IDENTIFIER,BRACE,ZERO,LITERAL_STRING,SINGLE_CHARACTER,PAREN,BRACKET,WHITESPACE,SEPARATE,SEMI,ASSIGN,BOOL_STRING,VARIABLE_TYPE,KEYWORD


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
 
    def PeekNextState(self, _input, _origin_digit=None): 
        # table에 input 들어가기전에 input 형태 변경해주기     
        if _input.isalpha() and self.GetTableName()=='IDENTIFIER' :
            _input='LETTER'

        elif _input.isalpha() and self.GetTableName()=='SINGLE_CHARACTER' :
           _input='LETTER'

        elif _input.isalpha() and self.GetTableName()=='LITERAL_STRING' :
            _input='LETTER' 
        
        elif _input.isdigit():
            if _input != '0':
                _input='EXCEPT_ZERO'


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
    inputString = inputString+" "
    f.close()
    # 우선순위 순으로 포함시켜야함 ! 
    transition_table_1=[ARITHMETIC_OPERATOR,SIGN_INTEGER,SINGLE_CHARACTER,LITERAL_STRING,IDENTIFIER,BRACE,PAREN,BRACKET,ZERO,COMPARISON_1,WHITESPACE,SEPARATE,SEMI,ASSIGN]
    # ,LITERAL_STRING,SINGLE_CHARACTER
    # COMPARISON - COMPARISON1이랑 COMPARISON2로 나누자 ..! 
    # COMPARISON_3,COMPARISON_2,COMPARISON_4,COMPARISON_5,
    transition_table_2=[BOOL_STRING,VARIABLE_TYPE,KEYWORD]

    dfa = FiniteAutomaton()

    temp_input_char = []
    temp_getTableName = ""
    

    for index, input_char in enumerate(inputString) :
        for i in range(0,len(transition_table_1)):
            dfa.LoadTransitionTable(transition_table_1[i])

            if temp_getTableName != "":
                
                if input_char.isdigit():
                    input_char="DIGIT"

                if dfa.GetTableName()==temp_getTableName:
                    nextState = dfa.PeekNextState(input_char)
                    dfa.SetState(nextState)

                    if dfa.IsAccepted():
                        next_index=index+1
                        next_input_char = inputString[next_index]
                        
                        if next_input_char.isdigit():
                            next_input_char="DIGIT"

                        next_input_state = dfa.PeekNextState(next_input_char)

                        # 원래 input 값 origin_input_char 변수에 두기
                        if input_char=='DIGIT':
                                origin_input_char=inputString[index]
                        else :
                            origin_input_char=input_char

                        if next_input_state != 'Unknown' and next_input_state != 'Rejected':
                            temp_input_char.append(origin_input_char)
                            temp_getTableName = dfa.GetTableName()
                            break
                        else:
                            temp_input_char.append(origin_input_char)
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
                                change_dfa.Reset()
                            else :
                                print("<",dfa.GetToken(),",",str_temp_input_char,">,")
                            
                            temp_input_char = [] #초기화
                            temp_getTableName = "" #초기화
                            dfa.Reset()
                            break
                    else :
                        #single character이나 literal 아직 끝마무리 안되었을때
                        next_index=index+1
                        next_input_char = inputString[next_index]

                        if next_input_char.isdigit():
                            next_input_char="DIGIT"

                        next_input_state = dfa.PeekNextState(next_input_char)

                        # 원래 input 값 origin_input_char 변수에 두기
                        if input_char=='DIGIT':
                                origin_input_char=inputString[index]
                        else :
                            origin_input_char=input_char

                        if next_input_state != 'Unknown' and next_input_state != 'Rejected':
                            temp_input_char.append(origin_input_char)
                            temp_getTableName = dfa.GetTableName()
                            break
                        else:
                            temp_input_char.append(origin_input_char)
                            str_temp_input_char=''.join(temp_input_char)
                            print("<",dfa.GetToken(),",",str_temp_input_char,">,")
                            
                            temp_input_char = [] #초기화
                            temp_getTableName = "" #초기화
                            dfa.Reset()
                            break

                else:
                    #if123같은 것들이 들어오는 경우에 해당하는 조건,,인가,,?
                    continue

            else :
                
                if dfa.PeekNextState(input_char)=="Unknown" :
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
                    
                    else:
                        #single_character이랑 literal_string 부분이 여기로 들어옴
                        try:
                            next_index=index+1
                            next_input_char = inputString[next_index]
                            if next_input_char.isdigit():
                                next_input_char="DIGIT"

                            next_input_state = dfa.PeekNextState(next_input_char)

                            if next_input_state != 'Unknown' and next_input_state != 'Rejected':
                                temp_input_char.append(input_char)
                                temp_getTableName = dfa.GetTableName()
                                break

                        except IndexError:
                            if dfa.GetToken()=="WHITESPACE":
                                    dfa.Reset()
                                    break
                            else:
                                pass
                                # print(input_char,11)
                                # print("<",dfa.GetToken(),",",input_char,">,,,")
