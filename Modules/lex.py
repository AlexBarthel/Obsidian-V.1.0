# import custom libraries
from std import sys
from Modules import getbuildinfo
from utils import format
from Parser import token
# defining a variable in a function is local to the function
# defining a variable in anywhere else in the program will be global
# defining a variable in a for / while loop is local to the loop

# variable stack
# variables = [global, local1, local2]
# push new varable dictionary to end when a function is called
# pop last dictionary off when a function finishes
# whenever creating new variable, add to last dictionary (most local)
# whenever changing existing variable, start with last dictionary and step back until you find it

LEXER_ERROR = False


class obsidian():
    def __init__(self, file_path, **warnings):
        # create default variables
        self.lexer_tokens = []

        # save the file path
        self.file_path = file_path

        # format the given file
        self.file = format.format(file_path)

        # default return value for __init__
        return None

    def _lex_line(self, line):
        # code here to lex a line, and return the tokens from that line
        global LEX_BUFFER, LEX_TOKENS;
        LEX_BUFFER = '';
        LEX_TOKENS = [];
        LEX_STRING = False;
        LEX_SYMBOLS = '+-/*%<>!:;()[]{},';
        LEX_COMPARISONS = ['==', '!=', '<=', '>=', '+=', '-=', '*=', '/=', '++', '--', '&&', '||'];

        def flushBuffer():
            global LEX_BUFFER, LEX_TOKENS
            if LEX_BUFFER != '':
                LEX_TOKENS.append(LEX_BUFFER)
            LEX_BUFFER = ''

        index = 0
        quote_type = ""
        while index < len(line):
            character = line[index]
            # Strings
            if (character == '"' or character == "'") and not LEX_STRING:
                flushBuffer()
                quote_type = character
                LEX_BUFFER += character
                LEX_STRING = True
                index += 1
                continue
            if LEX_STRING:
                if character == quote_type:
                    LEX_BUFFER += character
                    flushBuffer()
                    LEX_STRING = False
                else:
                    LEX_BUFFER += character
                index += 1
                continue

            if character == " ":
                flushBuffer()
            elif character in LEX_SYMBOLS:
                flushBuffer()
                if index < len(line) - 1:  #if not at end of line
                    if line[index:index+2] in LEX_COMPARISONS:  #if this+next char is a 2-char symbol
                        LEX_TOKENS.append(line[index:index + 2])
                        index += 1
                    else:
                        LEX_TOKENS.append(character)
                else:
                    LEX_TOKENS.append(character)
            else:
                LEX_BUFFER += character
            index += 1

        if LEX_BUFFER != "": LEX_TOKENS.append(LEX_BUFFER)
        return LEX_TOKENS


    def lex(self):
		# Issues:
		# Lexer won't seperate quotes from strings into tokens.
        for line in range(len(self.file)):
            lexed_line = self._lex_line(self.file[line]);
            print(line+1, end="\t| ")
            for t in lexed_line:
                print(token.ObsToken_OneChar(t), end=" ");
            print()
        return
