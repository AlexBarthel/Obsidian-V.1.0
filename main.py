# import custom libraries
from Modules import lex

# parse a file
#lexer = lex.obsidian('example/bugs.obs', version=0.1);
#lexer.lex();


# custom library testing

line = 'for (int a: 10; a >= 1; a--) {';
# line = '==>===.==' # this line is buggy
# line = '''
#     for (float i: 0.1; i >= -0.1; i-=0.05) {
#         display "Hello World!";
#     }
# '''; # this doesn't lex for some reason
###################################################################

LEX_BUFFER = "";
LEX_TOKENS = [];
LEX_STRING = False;
LEX_SYMBOLS = "+-/*%<>!:;()[]{},";
LEX_COMPARISONS = ['==', '!=', '<=', '>=', '+=', '-=', '*=', '/=', '++', '--', '&&', '||'];

def flushBuffer():
    global LEX_BUFFER, LEX_TOKENS;
    if LEX_BUFFER != '':
        LEX_TOKENS.append(LEX_BUFFER);
    LEX_BUFFER = '';

index = 0;
while index < len(line):
    character = line[index];
    # Strings
    if character == '"' and not LEX_STRING:
        flushBuffer();
        LEX_BUFFER += character;
        LEX_STRING = True;
        continue;
    if LEX_STRING: 
        if character == '"':
            LEX_BUFFER += character;
            flushBuffer();
            LEX_STRING = False;
        else: 
            LEX_BUFFER += character;
        continue;

    if character == " ":
        flushBuffer();
    elif character in LEX_SYMBOLS:
        flushBuffer();
        if index < len(line) - 1: #if not at end of line
            if line[index:index+2] in LEX_COMPARISONS: #if this+next char is a 2-char symbol
                LEX_TOKENS.append(line[index:index+2]);
                index += 1;
            else:
                LEX_TOKENS.append(character);
        else:
            LEX_TOKENS.append(character);
    else:
        LEX_BUFFER += character;
    index += 1;

if LEX_BUFFER != "": LEX_TOKENS.append(LEX_BUFFER);

from Parser import token
for t in LEX_TOKENS:
    print(token.ObsToken_OneChar(t));