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

if __name__=="__main__":
    f = open("./temp.txt", 'r')
    inputString = f.read()
    f.close()

    transition_table=[ARITHMETIC_OPERATOR]
    # for문으로 한번 크게 크게 돌기

    print("----tests----")
    for input_char in inputString :
        for i in range(0,len(transition_table)):
            dfa = FiniteAutomaton()
            dfa.LoadTransitionTable(transition_table[i])
            
            nextState = dfa.PeekNextState(input_char)
            dfa.SetState(nextState)
            #123 이렇게 들어가면 뭔지 생각해보자..
            if dfa.IsAccepted():
                print("<"+dfa.GetToken()+","+input_char+">,")
            else :
                dfa.Reset()