# import custom libraries
from std import sys
import Boolean
import String
import ArrayList
import Float
import Int

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
    'int': 'INT', 'float': 'FLOAT',
    'String': 'STRING', 'Boolean': 'BOOLEAN',
    'ArrayList': 'ARRAYLIST', 'void': 'VOID',
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


# for character in line:
#   if character is letter:
#     #variable type,          name,            function name
#     # space       , (colon, space, operator), parentheses
