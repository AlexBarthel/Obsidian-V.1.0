# import custom libraries
from Modules import lex

# tokenize a file
lexer = lex.obsidian('example/main.obs');
lexer.lex();

# the line to be lexed
line = 'for (int a: 10; a >= 1; a--) {';
