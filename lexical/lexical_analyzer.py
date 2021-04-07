from copy import copy

def check_prev_input(prev_input):
    if prev_input.isdigit():
        return "digit"
    else :
        return "noDigit"

class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}

 
    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates=_dfa["AcceptedStates"]
 
    def PeekNextState(self, _input, prev_input=None, temp=None):
        if _input.isdigit():
            if _input=='0':
                if prev_input=="noDigit" or prev_input==None :
                    pass
                else :
                    _input='DIGIT'
            else :
                if prev_input=="noDigit" or prev_input==None :
                    print(_input)
                    _input='EXCEPT_ZERO'
                else :
                    _input='DIGIT'
                    
        elif _input.isalpha() and len(_input)==1 :
            _input='LETTER'
        

        if not _input in self.table[self.currentState]:
            return "Unknown"
        
        nextState = self.table[self.currentState][_input]

        if nextState == "":
            return "Rejected"
        else:
            return nextState
    
    def GetFlag(self):
        return self.flag

    def SetFlag(self, _flag):
        self.flag =_flag

    def GetState(self):
        return self.currentState
        # 필요없을듯
 
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
 
    def Reset(self):
        self.currentState = "T0"
        self.consecutive_digit = 0
 
# Transition Table of Arithmetic Operator DFA
COMPARISON = {
    "AcceptedStates": {
        "T1": "COMPARISON",
        "T2": "COMPARISON",
        "T3": "COMPARISON",
        "T4": "COMPARISON",
        "T5": "COMPARISON",
        "T6": "COMPARISON",
    },
    "Table": {
        "T0": {">": "T1", "<": "T2", "==": "T3", "!=": "T4", ">=":"T5", "<=":"T6" },
        "T1": {">": "",   "<": "",   "==": "",   "!=": "",   ">=":"",   "<=":""  },
        "T2": {">": "",   "<": "",   "==": "",   "!=": "",   ">=":"",   "<=":""  },
        "T3": {">": "",   "<": "",   "==": "",   "!=": "",   ">=":"",   "<=":""  },
        "T4": {">": "",   "<": "",   "==": "",   "!=": "",   ">=":"",   "<=":""  },
        "T5": {">": "",   "<": "",   "==": "",   "!=": "",   ">=":"",   "<=":""  },
        "T6": {">": "",   "<": "",   "==": "",   "!=": "",   ">=":"",   "<=":""  },
    }
}


SIGN_INTEGER = {
    "AcceptedStates": {
        "T2": "INTEGER",
        "T3": "SIGN_INTEGER",
        "T4": "SIGN_INTEGER",
        "T5": "SIGN_INTEGER",
        "T6": "SIGN_INTEGER",
    },
    "Table": {
        "T0": {"-": "T1", "EXCEPT_ZERO": "T2", "DIGIT": "",   "0": "T3"},
        "T1": {"-": "",   "EXCEPT_ZERO": "T4", "DIGIT": "",   "0": ""  },
        "T2": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T5", "0": ""  },
        "T3": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "",   "0": ""  },
        "T4": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T6", "0": ""  },
        "T5": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T5", "0": ""  },
        "T6": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T6", "0": ""  },
    }
}

BRACE = {
    "AcceptedStates": {
        "T1": "LBRACE",
        "T2": "RBRACE",
    },
    "Table": {
        "T0": {"{": "T1", "}": "T2" },
        "T1": {"{": "",   "}": "",  },
        "T2": {"{": "",   "}": "",  },
    }
}

BRACKET= {
    "AcceptedStates": {
        "T1": "LBRACKET",
        "T2": "RBRACKET",
    },
    "Table": {
        "T0": {"[": "T1", "]": "T2" },
        "T1": {"[": "",   "]": "",  },
        "T2": {"[": "",   "]": "",  },
    }
}

WHITESPACE= {
    "AcceptedStates": {
        "T1": "WHITESPACE",
        "T2": "WHITESPACE",
        "T3": "WHITESPACE",
    },
    "Table": {
        "T0": {"\t": "T1", "\n": "T2", " ":"T3" },
        "T1": {"\t": "",   "\n": "",   " ":"T3" },
        "T2": {"\t": "",   "\n": "",   " ":"T3" },
        "T3": {"\t": "",   "\n": "",   " ":"T3" },
    }
}


ARITHMETIC_OPERATOR = {
    "AcceptedStates": {
        "T1": "OP",
        "T2": "OP",
        "T3": "OP",
        "T4": "OP",
    },
    "Table": {
        "T0": {"+": "T1", "-": "T2", "*": "T3", "/": "T4"},
        "T1": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T2": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T3": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T4": {"+": "",   "-": "",   "*": "",   "/": ""  },
    }
}

BOOL_STRING = {
    "AcceptedStates": {
        "T1": "BOOL_STRING",
        "T2": "BOOL_STRING",
    },
    "Table": {
        "T0": {"true": "T1", "false": "T2" },
        "T1": {"true": "",   "false": "",  },
        "T2": {"true": "",   "false": "",  },
    }
}

IDENTIFIER = {
    "AcceptedStates": {
        "T1": "IDENTIFIER",
        "T2": "IDENTIFIER",
        "T3": "IDENTIFIER",
        "T4": "IDENTIFIER",
        "T5": "IDENTIFIER",
    },
    "Table": {
        "T0": {"LETTER": "T1", "-": "T2", "DIGIT": "" },
        "T1": {"LETTER": "T3", "-": "T4", "DIGIT": "T5" },
        "T2": {"LETTER": "T3", "-": "T4", "DIGIT": "T5" },
        "T3": {"LETTER": "T3", "-": "T4", "DIGIT": "T5" },
        "T4": {"LETTER": "T3", "-": "T4", "DIGIT": "T5" },
    }
}



if __name__=="__main__":
    f = open("./lexical/temp.txt", 'r')
    inputString = f.read()
    f.close()

    # 우선순위 순으로 포함시켜야함 ! ex. keyword랑 identifier
    transition_table=[ARITHMETIC_OPERATOR,SIGN_INTEGER,IDENTIFIER,BRACE,BRACKET,COMPARISON,WHITESPACE,BOOL_STRING]

    temp_getToken = "" # 임시적으로 토큰이름을 저장해두는 변수
    temp_input_char = [] # 임시적으로 입력된 단일 문자를 저장해두는 리스트

    print("----test----")
    for input_char in inputString :
        # 단일문자가 아닌 symbol들을 묶어서 새롭게 split해야할듯 함
        # int, char, boolean, string, if, else, while, class, return, ==, !=, <=, \t, \n

        for i in range(0,len(transition_table)):
            dfa = FiniteAutomaton()
            dfa.LoadTransitionTable(transition_table[i])
            
            if dfa.PeekNextState(input_char)=="Unknown":
                dfa.Reset()

            else :
                index=inputString.find(input_char)
                
                nextState = dfa.PeekNextState(input_char)
                dfa.SetState(nextState)
                

                if dfa.IsAccepted():
                    # 현재도 accept token이지만 남은 input symbol이 있는지 확인하는 과정 (중요)
                    # 그다음 symbol을 입력받았을때(next_index변수 확인) accept한 경우엔 temp_input_char에 append해줌 (list추가) 
                    # 좀 자잘한 조건들이 있어서 if문이 많음 ㅇㅅㅇ..

                    next_index=index+1
                    
                    # 나중에 최적화하기
                    if next_index <= len(inputString) :
                        if next_index == len(inputString) :
                            if temp_getToken !="" :
                                print("<",temp_getToken,",",''.join(temp_input_char)+input_char,">,")
                                temp_getToken="" #초기화
                                temp_input_char=[] #초기화
                                dfa.Reset()
                            else :
                                print("< "+dfa.GetToken()+","+input_char+" >,")
                                dfa.Reset()

                        elif dfa.PeekNextState(inputString[next_index]) =='Rejected':
                            print("< "+dfa.GetToken()+","+input_char+" >,")
                            dfa.Reset()
                            break
                        
                        elif dfa.PeekNextState(inputString[next_index]) =='Unknown':
                            if dfa.GetToken()=="WHITESPACE":
                                break

                            if temp_getToken !="" :
                                print("<",temp_getToken,",",''.join(temp_input_char)+input_char,">,")
                                temp_getToken="" #초기화
                                temp_input_char=[] #초기화
                                dfa.Reset()
                            else :
                                print("< "+dfa.GetToken()+","+input_char+" >,")
                                dfa.Reset()
                                break
                        
                        else :
                            temp_getToken=dfa.GetToken() #T2
                            temp_input_char.append(input_char) #1,

                else :
                    if temp_getToken !="" :
                        print("<",''.join(temp_input_char)+input_char,",",temp_input_char,">,")
                        temp_getToken="" #초기화
                        temp_input_char=[] #초기화
                        dfa.Reset()
                    else :
                        dfa.Reset()





#-연산자 hidden problem

# 숫자 삽질하다가 날린 코드들 ~~
                # prev_index=index-1

                # prev_is_digit=None
                # if prev_index >=0 :
                #     prev_is_digit = check_prev_input(inputString[prev_index])
                # prev_is_digit = check_prev_input(inputString[index])

# dfd