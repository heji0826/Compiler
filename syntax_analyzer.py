Grammar_dic={ 'CODE': ['VDECL CODE', 'FDECL CODE', 'CDECL CODE’', ''], 'VDECL': ['vtype id semi', 'vtype ASSIGN semi'], 'ASSIGN': ['id assign RHS'], 'RHS': ['EXPR', 'literal', 'character', 'boolstr'], 'EXPR': ['T addsub EXPR', 'T'], 'T': ['F muldiv T', 'F'], 'F': ['lparen EXPR rparen', 'id', 'num'], 'FDECL': ['vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace'], 'ARG': ['vtype id MOREARGS', ''], 'MOREARGS': ['comma vtype id MOREARGS', ''], 'BLOCK': ['STMT BLOCK', ''], 'STMT': ['VDECL', 'ASSIGN semi', 'if lparen COND rparen lbrace BLOCK rbrace ELSE', 'while lparen COND rparen lbrace BLOCK rbrace'], 'COND': ['S comp S', 'S'], 'S': ['lparen COND rparen', 'boolstr'], 'ELSE': ['else lbrace BLOCK rbrace', ''],  'RETURN': ['return RHS semi'], 'CDECL': ['class id lbrace ODECL rbrace'], 'ODECL': ['VDECL ODECL', 'FDECL ODECL','']}

starting_symbol= 'CODE'

terminals=['vtype', 'num', 'character', 'boolstr', 'literal', 'id', 'if', 'else', 'while', 'return', 'class', 'addsub', 'muldiv', 'assign', 'comp', 'semi', 'comma', 'lparen', 'rparen', 'lbrace', 'rbrace']
nonterminals=['CODE', 'VDECL', 'ASSIGN','RHS', 'EXPR', 'T', 'F', 'FDECL', 'ARG', 'MOREARGS', 'BLOCK', 'STMT', 'COND', 'S', 'ELSE', 'RETURN', 'CDECL', 'ODECL']

parsing_table = {0: {'vtype': 's2', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': 1, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 1: {'vtype': 's6', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'s7', '$': 'r3', 'CODE': 3, 'VDECL': 1, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': 4, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': 5, 'ODECL': ''}, 2: {'vtype': '', 'id': 's8', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': 9, 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 3: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': 'acc', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 4: {'vtype': 's6', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'s7', '$': 'r3', 'CODE': 10, 'VDECL': 1, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': 4, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': 5, 'ODECL': ''}, 5: {'vtype': 's6', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'s7', '$': 'r3', 'CODE': 11, 'VDECL': 1, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': 4, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': 5, 'ODECL': ''}, 6: {'vtype': '', 'id': 's12', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': 9, 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 7: {'vtype': '', 'id': 's13', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 8: {'vtype': '', 'id': '', 'semi': 's14', 'assign': 's15', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 9: {'vtype': '', 'id': '', 'semi': 's16', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 10: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': 'r1', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 11: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': 'r2', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 12: {'vtype': '', 'id': '', 'semi': 's14', 'assign': 's15', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': 's17', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 13: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': 's18', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 14: {'vtype': 'r4', 'id': 'r4', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r4', 'comma': '', 'if': 'r4', 'while': 'r4', 'comp': '', 'else': '', 'return': 'r4', 'class':'r4', '$': 'r4', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 15: {'vtype': '', 'id': 's27', 'semi': '', 'assign': '', 'literal': 's21', 'character': 's22', 'boolstr': 's23', 'addsub': '', 'muldiv': '', 'lparen': 's26', 'rparen': '', 'num': 's28', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': 19, 'EXPR': 20, 'T': 24, 'F': 25, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 16: {'vtype': 'r5', 'id': 'r5', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r5', 'comma': '', 'if': 'r5', 'while': 'r5', 'comp': '', 'else': '', 'return': 'r5', 'class':'r5', '$': 'r5', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 17: {'vtype': 's30', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': 'r20', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': 29, 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 18: {'vtype': 's6', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r39', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': 32, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': 33, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': 31}, 19: {'vtype': '', 'id': '', 'semi': 'r6', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 20: {'vtype': '', 'id': '', 'semi': 'r7', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 21: {'vtype': '', 'id': '', 'semi': 'r8', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 22: {'vtype': '', 'id': '', 'semi': 'r9', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 23: {'vtype': '', 'id': '', 'semi': 'r10', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 24: {'vtype': '', 'id': '', 'semi': 'r12', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': 's34', 'muldiv': '', 'lparen': '', 'rparen': 'r12', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 25: {'vtype': '', 'id': '', 'semi': 'r14', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': 'r14', 'muldiv': 's35', 'lparen': '', 'rparen': 'r14', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 26: {'vtype': '', 'id': 's27', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': 's26', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': 36, 'T': 24, 'F': 25, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 27: {'vtype': '', 'id': '', 'semi': 'r16', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': 'r16', 'muldiv': 'r16', 'lparen': '', 'rparen': 'r16', 'num': 's28', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 28: {'vtype': '', 'id': '', 'semi': 'r17', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': 'r17', 'muldiv': 'r17', 'lparen': '', 'rparen': 'r17', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 29: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': 's37', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 30: {'vtype': '', 'id': 's38', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 31: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 's39', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 32: {'vtype': 's6', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r39', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': 32, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': 33, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': 40}, 33: {'vtype': 's6', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r39', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': 32, 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': 33, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': 41}, 34: {'vtype': '', 'id': 's27', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': 's26', 'rparen': '', 'num': 's28', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': 42, 'T': 24, 'F': 25, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 35: {'vtype': '', 'id': 's27', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': 's26', 'rparen': '', 'num': 's28', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': 43, 'F': 25, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 36: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': 's44', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 37: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': 's45', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 38: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': 'r22', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': 46, 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 39: {'vtype': 'r36', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': 's47', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class': 'r36', '$': 'r36', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 40: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r37', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 41: {'vtype': '', 'id': '', 'semi': '', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': '', 'num': '', 'lbrace': '', 'rbrace': 'r38', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 42: {'vtype': '', 'id': '', 'semi': 'r11', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': '', 'muldiv': '', 'lparen': '', 'rparen': 'r11', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 43: {'vtype': '', 'id': '', 'semi': 'r13', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': 'r13', 'muldiv': '', 'lparen': '', 'rparen': 'r13', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''}, 44: {'vtype': '', 'id': '', 'semi': 'r15', 'assign': '', 'literal': '', 'character': '', 'boolstr': '', 'addsub': 'r15', 'muldiv': 'r15', 'lparen': '', 'rparen': 'r15', 'num': '', 'lbrace': '', 'rbrace': '', 'comma': '', 'if': '', 'while': '', 'comp': '', 'else': '', 'return': '', 'class':'', '$': '', 'CODE': '', 'VDECL': '', 'ASSIGN': '', 'RHS': '', 'EXPR': '', 'T': '', 'F': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'COND': '', 'S': '', 'ELSE': '', 'RETURN': '', 'CDECL': '', 'ODECL': ''},
