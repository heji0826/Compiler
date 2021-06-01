# Transition Table of each token's DFA

COMPARISON_1 = {
    "Name" : "COMPARISON_1",
    "Table": {
        "T0": {">": "T1", "<": "T2"},
        "T1": {">": "",   "<": ""},
        "T2": {">": "",   "<": ""},
    },
    "AcceptTN": {
        "T1": "comp",
        "T2": "comp",
    },
}

COMPARISON_2 = {
    "Name" : "COMPARISON_2",
    "Table": {
        "T0": {"=": "T1"},
        "T1": {"=": "T2"},
        "T2": {"=": ""},
    },
    "AcceptTN": {
        "T2": "comp",
    },
}

COMPARISON_3 = {
    "Name" : "COMPARISON_3",
    "Table": {
        "T0": {"!": "T1", "=": ""},
        "T1": {"!": "",   "=": "T2"},
        "T2": {"!": "",   "=": ""},
    },
    "AcceptTN": {
        "T2": "comp",
    },
}

COMPARISON_4 = {
    "Name" : "COMPARISON_4",
    "Table": {
        "T0": {">": "T1", "=": ""},
        "T1": {">": "",   "=": "T2"},
        "T2": {">": "",   "=": ""},
    },
    "AcceptTN": {
        "T2": "comp",
    },
    
}

COMPARISON_5 = {
    "Name" : "COMPARISON_5",
    "Table": {
        "T0": {"<": "T1", "=": ""},
        "T1": {"<": "",   "=": "T2"},
        "T2": {"<": "",   "=": ""},
    },
    "AcceptTN": {
        "T2": "comp",
    },
    
}


SIGN_INTEGER = {
    "Name" : "SIGN_INTEGER",
    "Table": {
        "T0": {"-": "T1", "EXCEPT_ZERO": "T2", "DIGIT": ""},
        "T1": {"-": "",   "EXCEPT_ZERO": "T3", "DIGIT": ""},
        "T2": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T4"},
        "T3": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T5"},
        "T4": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T4"},
        "T5": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T5"},
    },
    "AcceptTN": {
        "T2": "num",
        "T3": "num",
        "T4": "num",
        "T5": "num",
    },
    
}

ZERO = {
    "Name" : "ZERO",
    "Table": {
        "T0": {"0": "T1"},
        "T1": {"0": ""},
    },
    "AcceptTN": {
        "T1": "num",
    },
    
}


BRACE = {
    "Name" : "BRACE",
    "Table": {
        "T0": {"{": "T1", "}": "T2" },
        "T1": {"{": "",   "}": "",  },
        "T2": {"{": "",   "}": "",  },
    },
    "AcceptTN": {
        "T1": "lbrace",
        "T2": "rbrace",
    },
    
}

PAREN = {
    "Name" : "PAREN",
    "Table": {
        "T0": {"(": "T1", ")": "T2" },
        "T1": {"(": "",   ")": "",  },
        "T2": {"(": "",   ")": "",  },
    },
    "AcceptTN": {
        "T1": "lparen",
        "T2": "rparen",
    },
    
}

BRACKET= {
    "Name" : "BRACKET",
    "Table": {
        "T0": {"[": "T1", "]": "T2" },
        "T1": {"[": "",   "]": "",  },
        "T2": {"[": "",   "]": "",  },
    },
    "AcceptTN": {
        "T1": "lbracket",
        "T2": "rbracket",
    },
    
}

WHITESPACE= {
    "Name" : "WHITESPACE",
    "Table": {
        "T0": {"\t": "T1", "\n": "T2", " ":"T3" },
        "T1": {"\t": "",   "\n": "",   " ":"" },
        "T2": {"\t": "",   "\n": "",   " ":"" },
        "T3": {"\t": "",   "\n": "",   " ":"" },
    },
    "AcceptTN": {
        "T1": "WHITESPACE",
        "T2": "WHITESPACE",
        "T3": "WHITESPACE",
    },
    
}

ARITHMETIC_OPERATOR = {
    "Name" : "ARITHMETIC_OPERATOR",
    "Table": {
        "T0": {"+": "T1", "-": "T2", "*": "T3", "/": "T4"},
        "T1": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T2": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T3": {"+": "",   "-": "",   "*": "",   "/": ""  },
        "T4": {"+": "",   "-": "",   "*": "",   "/": ""  },
    },
    "AcceptTN": {
        "T1": "addsub",
        "T2": "addsub",
        "T3": "multdiv",
        "T4": "multdiv",
    },
    
}

BOOL = {
    "Name" : "BOOL",
    "Table": {
        "T0": {"true": "T1", "false": "T2" },
        "T1": {"true": "",   "false": "",  },
        "T2": {"true": "",   "false": "",  },
    },
    "AcceptTN": {
        "T1": "boolstr",
        "T2": "boolstr",
    },
    
}



ID = {
    "Name" : "ID",
    "Table": {
        "T0": {"LETTER": "T1", "_": "T2", "DIGIT": "" },
        "T1": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T2": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T3": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T4": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
        "T5": {"LETTER": "T3", "_": "T4", "DIGIT": "T5" },
    },
    "AcceptTN": {
        "T1": "id",
        "T2": "id",
        "T3": "id",
        "T4": "id",
        "T5": "id",
    },
    
}

VARIABLE_TYPE = {
    "Name" : "VARIABLE_TYPE",
    "Table": {
        "T0": {"int": "T1", "char": "T2", "boolean": "T3", "string":"T4" },
        "T1": {"int": "", "char": "", "boolean": "", "string":"" },
        "T2": {"int": "", "char": "", "boolean": "", "string":"" },
        "T3": {"int": "", "char": "", "boolean": "", "string":"" },
        "T4": {"int": "", "char": "", "boolean": "", "string":"" },
    },
    "AcceptTN": {
        "T1": "vtype",
        "T2": "vtype",
        "T3": "vtype",
        "T4": "vtype",
    },
    
}

SINGLE_CHARACTER = {
    "Name" : "SINGLE_CHARACTER",
    "Table": {
        "T0": {"'": "T1", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T1": {"'": "", "DIGIT": "T2", "LETTER": "T3", "SYMBOL":"T4", " ":"T5" },
        "T2": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T3": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T4": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T5": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T6": {"'": "", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
    },
    "AcceptTN": {
        "T6": "character",
    },
    
}

LITERAL_STRING = {
    "Name" : "LITERAL_STRING",
    "Table": {
        "T0": { "DIGIT": "", "LETTER": "", " ":"" ,'"': "T1"},
        "T1": {'"': "", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T2": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T3": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T4": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T5": {'"': "", "DIGIT": "", "LETTER": "", " ":"" },
    },
    "AcceptTN": {
        "T5": "literal",
    },
    
}

KEYWORD = {
    "Name" : "KEYWORD",
    "Table": {
        "T0": {"if": "T1", "else": "T2", "while": "T3", "class":"T4", "return":"T5" },
        "T1": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T2": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T3": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T4": {"if": "", "else": "", "while": "", "class":"", "return":"" },
        "T5": {"if": "", "else": "", "while": "", "class":"", "return":"" },
    },
    "AcceptTN": {
        "T1": "if",
        "T2": "else",
        "T3": "while",
        "T4": "class",
        "T5": "return",
    },
    
}

ASSIGN= {
    "Name" : "ASSIGN",
    "Table": {
        "T0": {"=": "T1"},
        "T1": {"=": ""},
    },
    "AcceptTN": {
        "T1": "assign",
    },
    
}

SEMI= {
    "Name" : "SEMI",
    "Table": {
        "T0": {";": "T1"},
        "T1": {";": ""},
    },
    "AcceptTN": {
        "T1": "semi",
    },
    
}

SEPARATE= {
    "Name" : "SEPARATE",
    "Table": {
        "T0": {",": "T1"},
        "T1": {",": ""},
    },
    "AcceptTN": {
        "T1": "comma",
    },
    
}

DDAOM_ERROR = {
    "Name" : "DDAOM_ERROR",
    "Table": {
        "T0": {"'": "T1", '"': "T2" },
        "T1": {"'": "T3", '"': "" },
        "T2": {"'": "", '"': "T3" },
        "T3": {"'": "", '"': "" },
    },
    "AcceptTN": {
        "T3": "Error",
    },
    
}