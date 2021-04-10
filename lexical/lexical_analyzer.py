class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
        self.tableName = {}

    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates=_dfa["AcceptedStates"]
        self.tableName =_dfa["Name"]

    def GetTableName(self):
        return self.tableName
 
    def PeekNextState(self, _input):
        # if _input.isdigit():
        #     if _input=='0':
        #         _input='DIGIT'
        #     else :
        #         _input='EXCEPT_ZERO'
        #         # _input='DIGIT'
        # 숫자 아직 하는 중..
                    
        if _input.isalpha() and self.GetTableName()=='IDENTIFIER' :
            # 혜지양 조건문에 self.GetTableName== single_character or literal_string 추가해야할듯?!?
            _input='LETTER'
        

        if not _input in self.table[self.currentState]:
            return "Unknown"
        
        nextState = self.table[self.currentState][_input]

        if nextState == "":
            return "Rejected"
        else:
            return nextState
    
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
 
# Transition Table of each token's DFA
COMPARISON = {
    "Name" : "COMPARISON",
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
    "Name" : "SIGN_INTEGER",
    "AcceptedStates": {
        "T2": "INTEGER",
        "T3": "INTEGER",
        "T4": "INTEGER",
        "T5": "INTEGER",
        "T6": "INTEGER",
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
    "Name" : "BRACE",
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

PAREN = {
    "Name" : "PAREN",
    "AcceptedStates": {
        "T1": "LPAREN",
        "T2": "RPAREN",
    },
    "Table": {
        "T0": {"(": "T1", ")": "T2" },
        "T1": {"(": "",   ")": "",  },
        "T2": {"(": "",   ")": "",  },
    }
}

BRACKET= {
    "Name" : "BRACKET",
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
    "Name" : "WHITESPACE",
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
    "Name" : "ARITHMETIC_OPERATOR",
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
    "Name" : "BOOL_STRING",
    "AcceptedStates": {
        "T1": "BOOL",
        "T2": "BOOL",
    },
    "Table": {
        "T0": {"true": "T1", "false": "T2" },
        "T1": {"true": "",   "false": "",  },
        "T2": {"true": "",   "false": "",  },
    }
}

IDENTIFIER = {
    "Name" : "IDENTIFIER",
    "AcceptedStates": {
        "T1": "ID",
        "T2": "ID",
        "T3": "ID",
        "T4": "ID",
        "T5": "ID",
    },
    "Table": {
        "T0": {"LETTER": "T1", "_": "T2", "DIGIT": "" },
        "T1": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T2": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T3": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T4": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T5": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
    }
}

VARIABLE_TYPE = {
    "Name" : "VARIABLE_TYPE",
    "AcceptedStates": {
        "T1": "VT",
        "T2": "VT",
        "T3": "VT",
        "T4": "VT",
    },
    "Table": {
        "T0": {"int": "T1", "char": "T2", "boolean": "T3", "string":"T4" },
        "T1": {"int": "", "char": "", "boolean": "", "string":"" },
        "T2": {"int": "", "char": "", "boolean": "", "string":"" },
        "T3": {"int": "", "char": "", "boolean": "", "string":"" },
        "T4": {"int": "", "char": "", "boolean": "", "string":"" },
    }
}

SINGLE_CHARACTER = {
    "Name" : "SINGLE_CHARACTER",
    "AcceptedStates": {
        "T6": "SINGLE",
    },
    "Table": {
        "T0": {"'": "T1", "DIGIT": "", "LETTER": "", "SYMBOL":"", "BLANK":"" },
        "T1": {"'": "", "DIGIT": "T2", "LETTER": "T3", "SYMBOL":"T4", "BLANK":"T5" },
        "T2": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", "BLANK":"" },
        "T3": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", "BLANK":"" },
        "T4": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", "BLANK":"" },
        "T5": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", "BLANK":"" },
        "T6": {"'": "", "DIGIT": "", "LETTER": "", "SYMBOL":"", "BLANK":"" },
    }
}

LITERAL_STRING = {
    "Name" : "LITERAL_STRING",
    "AcceptedStates": {
        "T5": "LITERAL",
    },
    "Table": {
        "T0": {""": "T1", "DIGIT": "", "LETTER": "", "BLANK":"" },
        "T1": {""": "T5", "DIGIT": "T3", "LETTER": "T2", "BLANK":"T4" },
        "T2": {""": "T5", "DIGIT": "T3", "LETTER": "T2", "BLANK":"T4" },
        "T3": {""": "T5", "DIGIT": "T3", "LETTER": "T2", "BLANK":"T4" },
        "T4": {""": "T5", "DIGIT": "T3", "LETTER": "T2", "BLANK":"T4" },
        "T5": {""": "", "DIGIT": "", "LETTER": "", "BLANK":"" },
    }
}

KEYWORD = {
    "Name" : "KEYWORD",
    "AcceptedStates": {
        "T1": "KEYWORD",
        "T2": "KEYWORD",
        "T3": "KEYWORD",
        "T4": "KEYWORD",
        "T5": "KEYWORD",
    },
    "Table": {
        "T0": {"if": "T1", "else": "T2", "while": "T3", "class":"T4", "return":"T5" },
        "T1": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T2": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T3": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T4": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T5": {"if": "", "else": "", "while": "", "class":"", "return":"" },
    }
}

ASSIGNMENT= {
    "Name" : "ASSIGNMENT",
    "AcceptedStates": {
        "T1": "ASSIGNMENT",
    },
    "Table": {
        "T0": {"=": "T1"},
        "T1": {"=": ""},
    }
}

TERMINATE= {
    "Name" : "TERMINATE",
    "AcceptedStates": {
        "T1": "TERMINATE",
    },
    "Table": {
        "T0": {";": "T1"},
        "T1": {";": ""},
    }
}

SEPARATE= {
    "Name" : "SEPARATE",
    "AcceptedStates": {
        "T1": "SEPARATE",
    },
    "Table": {
        "T0": {",": "T1"},
        "T1": {",": ""},
    }
}

if __name__=="__main__":
    f = open("./lexical/temp.txt", 'r')
    inputString = f.read()
    f.close()
    
    # 우선순위 순으로 포함시켜야함 ! ex. keyword랑 identifier
    transition_table=[ARITHMETIC_OPERATOR,SIGN_INTEGER,IDENTIFIER,SINGLE_CHARACTER,BRACE,PAREN,BRACKET,COMPARISON,WHITESPACE,BOOL_STRING,SEPARATE,TERMINATE,ASSIGNMENT]

    temp_getToken = "" # 임시적으로 토큰이름을 저장해두는 변수
    temp_input_char = [] # 임시적으로 입력된 단일 문자를 저장해두는 리스트

    for input_char in inputString :
        for i in range(0,len(transition_table)):
            dfa = FiniteAutomaton()
            dfa.LoadTransitionTable(transition_table[i])
            
            index=inputString.find(input_char)

            if dfa.PeekNextState(input_char)=="Unknown":
                dfa.Reset()

            else :
                index=inputString.find(input_char)
                
                nextState = dfa.PeekNextState(input_char)
                dfa.SetState(nextState)
                
                if dfa.IsAccepted():
                    # 현재도 accept token이지만 남은 input symbol이 있는지 확인하는 과정 (중요)
                    # 그다음 symbol을 입력받았을때(next_index변수 확인) accept한 경우엔 temp_input_char에 append해줌 (list추가) 

                    next_index=index+1

                    if next_index < len(inputString) :

                        peekNextState = dfa.PeekNextState(inputString[next_index])
                        
                        if peekNextState =='Rejected' or peekNextState =='Unknown' :
                            if dfa.GetToken()=="WHITESPACE":
                                pass
                            elif temp_getToken !="" :
                                print("<",temp_getToken,",",''.join(temp_input_char)+input_char,">,")
                                temp_getToken="" #초기화
                                temp_input_char=[] #초기화
                                dfa.Reset()
                            else :
                                print("< "+dfa.GetToken()+","+input_char+" >,")
                                dfa.Reset()
                        
                        else :
                            temp_getToken=dfa.GetToken() 
                            temp_input_char.append(input_char) 

                        break
                    
                    else :
                        if temp_getToken !="" :
                            print("<",temp_getToken,",",''.join(temp_input_char)+input_char,">,")
                            temp_getToken="" #초기화
                            temp_input_char=[] #초기화
                            dfa.Reset()
                        else :
                            print("< "+dfa.GetToken()+","+input_char+" >,")
                            dfa.Reset()
                else :
                    if temp_getToken !="" :
                        print("<",''.join(temp_input_char)+input_char,",",temp_input_char,">,")
                        temp_getToken="" #초기화
                        temp_input_char=[] #초기화
                    dfa.Reset()





#-연산자 hidden problem