# import custom libraries
from std import sys
from Modules import getbuildinfo
from utils import format

# defining a variable in a function is local to the function
# defining a variable in anywhere else in the program will be global
# defining a variable in a for / while loop is local to the loop

#void main(globals) {
#   String num: '1';
#   void function1(locals) {
#       int a: 0;
#       int b: 2;
#       void function2(locals) {
#           int c: 3;
#           a: 4;
#           num: '6';
#       }
#   }
#   void function3(locals) {
#       ArrayList d: [1, 3, 2];
#       display d[0];
#   }
#   num: '4';
#}
#
# variables = [{"num": "6"},"LIST":["1"]]

# variable stack
# variables = [global, local1, local2]
# push new varable dictionary to end when a function is called
# pop last dictionary off when a function finishes
# whenever creating new variable, add to last dictionary (most local)
# whenever changing existing variable, start with last dictionary and step back until you find it

# TODO:
# - lambda functions
# - variable stacking
variables = [{}]
LEXER_ERROR = False

class obsidian():
    def __init__(self, file_path, version, **warnings):
        # create default variables
        self.lexer_tokens = []
        self.TOKENS = (
            'NAME',
            'PLUS', 'MINUS',
            'TIMES', 'DIVIDE',
            'FLOAT', 'INT',
            'STRING', 'BOOLEAN',
            'ARRAYLIST', 'VOID',
        );

        self.T_IGNORE = ' \t';
        self.T_NEWLINE = '\n';

        # save the file path
        self.file_path = file_path

        # format the given file
        self.file = format.format(file_path)
        if self.file == None: return None

        # default return value for __init__
        return None
    
    def lex_variable(self, t_line, lineno):
        t_token = {'TYPE': '', 'NAME': '', 'VALUE': ''};

        for TOKEN in self.TOKENS:
            if (t_line[0].upper() == TOKEN):
                t_token['TYPE'] = TOKEN;
                break;
        t_line[1] = t_line[1].strip(':')
        for CHARACTER in t_line[1]:
            t_token['NAME'] += CHARACTER;

        t_line[2] = t_line[2].rstrip(';')
        for CHARACTER in t_line[2]:
            t_token['VALUE'] += CHARACTER;

        return t_token;
            

    def lex_line(self, l_line, lineno):
        lBuffer = "";
        lTokens = [];
        lStringifying = False;
        lSymbols = "+-/*%<>!:;()[]{},";
        lComparisons = ['==', '!=', '<=', '>=', '+=', '-=', '*=', '/=', '++', '--', '&&', '||'];

        def flushBuffer():
            global lBuffer, lTokens;
            if lBuffer != '':
                lTokens.append(lBuffer);
            lBuffer = '';

    def lex_string(self, t_line, lineno):
        print()
    def lex_equation(self, t_line, lineno):
        print()

    def lex(self):
        getbuildinfo.Obs_GetBuildInfo()
        for lineno in range(len(self.file)):
            current_line = self.file[lineno].split(' ');
            
            t_line = [];
            for TOKEN in current_line:
                if (TOKEN in self.T_IGNORE): continue
                else: t_line.append(TOKEN);

            if len(t_line) > 0:
                t_line[0] = t_line[0].strip('\t')
                if (t_line[0] == '*'):
                    continue
                else:
                    for t in t_line:
                        t = t.strip(':').strip(';')
                        print(token.ObsToken_OneChar(t), end=' ')
                if LEXER_ERROR: break;
                print()
                
