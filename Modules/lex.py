# import custom libraries
from std import sys
from Modules import getbuildinfo
from utils import format

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
    def __init__(self, file_path, version, **warnings):
        # create default variables
        self.lexer_tokens = [];

        # save the file path
        self.file_path = file_path;

        # format the given file
        self.file = format.format(file_path);

        # default return value for __init__
        return None;

    def lex_line(self, l_line, lineno):
        # code here to lex a line, and return the tokens from that line
        return;

    def lex(self):
		# code here that breaks up the lines and sends them to the lex_line function
        return;