print(f'{str(__file__).replace("/", ".")[1:]} imported')
# import custom libraries
from Modules import lex

# colors
COLORS = ['\033[31m','\033[33m'];
ESCAPE = '\033[0m';

# preferences
SYS_WARNINGS = True;


def warning(message):
    if SYS_WARNINGS:
        print(f'{COLORS[1]}WARNING: {message}{ESCAPE}');


def end(err, file, lineno):
    print('\nFile "%s", line %d, in <module>' % (file.split("/")[-1], lineno));
    print("\t%s" % err);
    lex.LEXER_ERROR = True;


def println(values, e):
	print(values, end=e);

def RAISE_SYNTAX_ERROR(error, o):
    print(f"SyntaxError: {error} \n\t{o}");

