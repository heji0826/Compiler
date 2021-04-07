class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
 
    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates.update(_dfa["AcceptedStates"])
 
    def PeekNextState(self, _input):
        # digit 들어오면 input str 말고 숫자로 형변환하거나, 'digit'으로 바꾸거나 하기
        if _input.isdigit():
            if _input==0:
                _input='DIGIT'
            else :
                _input='EXCEPT_ZERO'
        
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
        "T1": "true",
        "T2": "false",
    },
    "Table": {
        "T0": {"true": "T1", "false": "T2" },
        "T1": {"true": "",   "false": "",  },
        "T2": {"true": "",   "false": "",  },
    }
}


if __name__=="__main__":
    f = open("./lexical/temp.txt", 'r')
    inputString = f.read()
    f.close()

    transition_table=[ARITHMETIC_OPERATOR,SIGN_INTEGER]

    print("----test----")
    for input_char in inputString :
        for i in range(0,len(transition_table)):
            dfa = FiniteAutomaton()
            dfa.LoadTransitionTable(transition_table[i])

            if dfa.PeekNextState(input_char)=="Unknown":
                dfa.Reset()
            else :
                nextState = dfa.PeekNextState(input_char)
                dfa.SetState(nextState)
                #input char 하나가 아니라 여러개가 모여서 만들어지는 token 구하려면 뭘 더 추가해야할듯..

                if dfa.IsAccepted():
                    if dfa.GetToken=="WHITETOKEN":
                        pass
                    else :
                        print("<"+dfa.GetToken()+","+input_char+">,")
                    dfa.Reset()
                    break
                else :
                    dfa.Reset()