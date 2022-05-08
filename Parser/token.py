# import custom libraries
from Modules import (
	Int, 
	Float, 
	String, 
	Boolean, 
	ArrayList
)

# Token names

_ObsParser_TokenNames = {
    # escape sequences
    '\n': 'NEWLINE', '\t': 'INDENT',
    '\\': 'BACKSLASH',
    # delimeters
    '(': 'LPAREN', ')': 'RPAREN',
    '[': 'LBRACKET', ']': 'RBRACKET',
    '{': 'LBRACE', '}': 'RBRACE',
    # termination characters
    ':': 'COLON', ';': 'SEMI',
    ',': 'COMMA',  '.': 'DOT',
    # operators
    '+': 'PLUS', '-': 'MINUS',
    '*': 'STAR', '/': 'SLASH', '%': 'MOD',
    '<': 'LESS', '>': 'GREATER',
    '!': 'NOT',
    # two char operators
    '==': 'EQUALEQUAL', '!=': 'NOTEQUAL',
    '<=': 'LESSEQUAL', '>=': 'GREATEREQUAL',
    '+=': 'PLUSEQUAL', '-=': 'MINUSEQUAL',
    '*=': 'STAREQUAL', '/=': 'SLASHEQUAL',
    '++': 'PLUSPLUS', '--': 'MINUSMINUS',
    '&&': 'AND', '||': 'OR',
    # data types
    'int': 'tINT', 'float': 'tFLOAT',
    'String': 'tSTRING', 'Boolean': 'tBOOLEAN',
    'ArrayList': 'tARRAYLIST', 'void': 'tVOID',
	'vector2': 'tVECTOR2', 'vector3': 'tVECTOR3',
    # conditionals
    'if': 'IF', 'else': 'ELSE',
    # loops
    'for': 'FOR', 'while': 'WHILE',
    # display
    'display': 'DISPLAY',
    'use': 'USE'
};

def ObsToken_OneChar(c1):
    if c1 not in list(_ObsParser_TokenNames.keys()):
        if Int.parseInt(c1): # INT eval
            return f'INT({c1})';
        if Float.parseFloat(c1): # FLOAT eval
            return f'FLOAT({c1})';
        if Boolean.parseBoolean(c1):
            return f'BOOLEAN({c1})'; 
        if String.parseString(c1):
            return f'STRING({c1})';
        if ArrayList.parseArrayList(c1):
            return f'ARRAYLIST({c1})';
        # variable name, value, function name
        # myFunction(a,
        return f'NAME({c1})';
    if c1 != "\n":
        return _ObsParser_TokenNames[c1]+f"({c1})";
    else: return _ObsParser_TokenNames[c1]+f"(\\n)";

