# import custom libraries
import _sys
from Modules import getbuildinfo
from utils import format

# defining a variable in a function is local to the function
# defining a variable in anywhere else in the program will be global
# defining a variable in a for / while loop is local to the loop
# main (globals)
# 	string num = "1"
# 	function1 (locals)
# 		int a = 0
# 		int b = 2
# 		function2 (locals)
# 			int c = 3
# 			a = 4
# 			num = "6"
# 	function3 (locals)
# 		int d = 4function3 (locals)
# 		int d = 4
# 	LIST = ["1"]
# }

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
PARSER_ERROR = False

def parse(file, version, warnings):
    # set the preference for alerts
    _sys.SYS_WARNINGS = warnings

    # check the current git repo
    if version > getbuildinfo.GITVERSION:
        _sys.end(
            f'GitError: Git repo {version} does not exist.',
            __file__, 0
        )
    elif version != getbuildinfo.GITVERSION:
        _sys.warning(
            f'You are using obs+ version {version}; however, version {getbuildinfo.GITVERSION} is available.'
            % (str(version), str(getbuildinfo.GITVERSION)))
        getbuildinfo.GITVERSION = version

    # format the given file
    file = format.format(file)
    if file == None: return []
    parser_tokens = []


    # iterate over all the lines in the file and tokenize
    for lineno in range(0, len(file)):
        cur_line = file[lineno].lstrip('\t').lstrip(' ');
        for whitespace_token in cur_line.split(" "):
            whitespace_token = whitespace_token.strip(' ')
            for colon_token in whitespace_token.split(":"):
                colon_token = colon_token.strip(' ')
                if colon_token != '':
                    print("Token:", colon_token, "| LINENO:", lineno)
        # find the token and value
        line_tokens = cur_line.split(':');
        if line_tokens[0][0:1] == '*': continue;
        if len(line_tokens) == 1:  # evaluate / call a function
            # tokenize for function parsing
            pass
        elif len(line_tokens) > 1:  # evaluate/change a variable
            # tokenize for variable parsing
            token = line_tokens[0].rstrip(' ');
            variable_tokens = token.split(' ');

            # predefine variables in proper scope
            variable_type = variable_name = '';
            variable_value = line_tokens[1].lstrip(' ').lstrip('\t').rstrip(";");
            if len(variable_tokens) > 1:  # evaluate a new variable
                variable_type = variable_tokens[0];
                # throw an error
                if variable_type == '':
                    _sys.end(
                        "SyntaxError: invalid syntax",
                        __file__, lineno + 1
                    );
                    break;
                variable_name = variable_tokens[1];
                
                # Add the variable to the top of the stack
                variables[len(variables) - 1][variable_name] = variable_type;

            elif len(variable_tokens) == 1:  # change an existing variable
                # predefine variables in proper scope
                variable_type = '';
                variable_name = variable_tokens[0];

                # search through the stack to find the matching variable name
                for scope in variables:
                    for var_name in scope.keys():
                        if var_name == variable_name:
                            variable_type = scope.get(var_name);
                # throw an error
                if variable_type == '':
                    _sys.end(
                        "NameError: name '%s' is not defined" % variable_name,
                        __file__, lineno + 1
                    );
                    break;
                # add a type error
            if variable_type == 'int':
                # use eval if the variable is a num or string
                parser_tokens.append({
                    'TYPE': variable_type,
                    'NAME': variable_name,
                    'VALUE': eval(variable_value),
                });
            else:
                parser_tokens.append({
                    'TYPE': variable_type,
                    'NAME': variable_name,
                    'VALUE': variable_value,
                });
    if PARSER_ERROR == True:
        return []
    else:
        # get the current GITVERSION build info
        getbuildinfo.GITVERSION = version
        getbuildinfo.Obs_GetBuildInfo()
        return parser_tokens
