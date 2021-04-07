class FiniteAutomaton:
    def __init__(self):
        self.table = {}
        self.currentState = "T0"
        self.acceptedStates = {}
 
    def LoadTransitionTable(self, _dfa):
        self.table = _dfa["Table"]
        self.acceptedStates.update(_dfa["AcceptedStates"])
 
    def PeekNextState(self, _input):
        if not _input in self.table[self.currentState]:
            print("Unknown Input Symbol is Given.")
            exit()
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
 
    def Reset(self):
        self.currentState = "T0"
 
# Transition Table of Arithmetic Operator DFA
ARITHMETIC_OPERATOR = {
    # 들어와서 isdigit? true면 무조건 'digit'라고 바꾸는거지 
    "AcceptedStates": {
        "T1": "ArithmeticOperator플러스",
        "T2": "ArithmeticOperator마이너스",
        "T3": "ArithmeticOperator곱하기",
        "T4": "ArithmeticOperator나누기"
    },
    "Table": {
        "T0": {"+": "T1", "-": "T2", "*": "T3", "/": "T4"},
        "T1": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T2": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T3": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T4": {"+": "",   "-": "",   "*": "",   "/": ""  },
    }
}

if __name__=="__main__":
    # DFA를 ARITHMETIC_OPERATOR로 초기화
    dfa = FiniteAutomaton()
    dfa.LoadTransitionTable(ARITHMETIC_OPERATOR)
    # DFA 사용
    print("---TEST---")
    print("Input이 \"*\"일 때")
    input_char = "ㅁ" #파일을 읽는거야..
    nextState = dfa.PeekNextState(input_char)
    dfa.SetState(nextState)
    print("Accepted State입니까?", dfa.IsAccepted())
    print("나의 현재 State:", dfa.GetState())
    print("토큰이 {}로 분류되었습니다.".format(dfa.GetToken()))
    # dfa를 사용을 마쳤으면 종료
    dfa.Reset()
    print("-----------")