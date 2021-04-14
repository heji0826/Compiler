# Transition Table of each token's DFA

COMPARISON_1 = {
    "Name" : "COMPARISON_1",
    "AcceptedStates": {
        "T1": "COMPARISON",
        "T2": "COMPARISON",
    },
    "Table": {
        "T0": {"<": "T1", ">": "T2"},
        "T1": {"<": "",   ">": ""},
        "T2": {"<": "",   ">": ""},
    }
}

COMPARISON_2 = {
    "Name" : "COMPARISON_2",
    "AcceptedStates": {
        "T2": "COMPARISON",
    },
    "Table": {
        "T0": {"=": "T1"},
        "T1": {"=": "T2"},
        "T2": {"=": ""},
    }
}

COMPARISON_3 = {
    "Name" : "COMPARISON_3",
    "AcceptedStates": {
        "T2": "COMPARISON",
    },
    "Table": {
        "T0": {"!": "T1", "=": ""},
        "T1": {"!": "",   "=": "T2"},
        "T2": {"!": "",   "=": ""},
    }
}

COMPARISON_4 = {
    "Name" : "COMPARISON_4",
    "AcceptedStates": {
        "T2": "COMPARISON",
    },
    "Table": {
        "T0": {">": "T1", "=": ""},
        "T1": {">": "",   "=": "T2"},
        "T2": {">": "",   "=": ""},
    }
}

COMPARISON_5 = {
    "Name" : "COMPARISON_5",
    "AcceptedStates": {
        "T2": "COMPARISON",
    },
    "Table": {
        "T0": {"<": "T1", "=": ""},
        "T1": {"<": "",   "=": "T2"},
        "T2": {"<": "",   "=": ""},
    }
}


SIGN_INTEGER = {
    "Name" : "SIGN_INTEGER",
    "AcceptedStates": {
        "T2": "INTEGER",
        "T3": "INTEGER",
        "T4": "INTEGER",
        "T5": "INTEGER",
    },
    "Table": {
        "T0": {"-": "T1", "EXCEPT_ZERO": "T2", "DIGIT": ""},
        "T1": {"-": "",   "EXCEPT_ZERO": "T3", "DIGIT": ""},
        "T2": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T4"},
        "T3": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T5"},
        "T4": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T4"},
        "T5": {"-": "",   "EXCEPT_ZERO": "",   "DIGIT": "T5"},
    }
}

ZERO = {
    "Name" : "ZERO",
    "AcceptedStates": {
        "T1": "INTEGER",
    },
    "Table": {
        "T0": {"0": "T1"},
        "T1": {"0": ""},
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
        "T1": {"\t": "",   "\n": "",   " ":"" },
        "T2": {"\t": "",   "\n": "",   " ":"" },
        "T3": {"\t": "",   "\n": "",   " ":"" },
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
        "T1": "VTYPE",
        "T2": "VTYPE",
        "T3": "VTYPE",
        "T4": "VTYPE",
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
        "T0": {"'": "T1", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T1": {"'": "", "DIGIT": "T2", "LETTER": "T3", "SYMBOL":"T4", " ":"T5" },
        "T2": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T3": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T4": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T5": {"'": "T6", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
        "T6": {"'": "", "DIGIT": "", "LETTER": "", "SYMBOL":"", " ":"" },
    }
}

LITERAL_STRING = {
    "Name" : "LITERAL_STRING",
    "AcceptedStates": {
        "T5": "LITERAL",
    },
    "Table": {
        "T0": { "DIGIT": "", "LETTER": "", " ":"" ,'"': "T1"},
        "T1": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T2": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T3": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T4": {'"': "T5", "DIGIT": "T3", "LETTER": "T2", " ":"T4" },
        "T5": {'"': "", "DIGIT": "", "LETTER": "", " ":"" },
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

ASSIGN= {
    "Name" : "ASSIGN",
    "AcceptedStates": {
        "T1": "ASSIGN",
    },
    "Table": {
        "T0": {"=": "T1"},
        "T1": {"=": ""},
    }
}

SEMI= {
    "Name" : "SEMI",
    "AcceptedStates": {
        "T1": "SEMI",
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
