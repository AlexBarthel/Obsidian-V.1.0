# import custom libraries
from std import sys

def format(file):
    content = [];
	# open the file
    try:
        with open(file, 'r') as f:
            content.append(f.readlines());
        content = content[0];
		# remove '\n' from the end of each line
        # for lineno in range(0, len(content)):
        #     content[lineno] = content[lineno].strip('\n');
		# return content
        return content;
    except FileNotFoundError:
        sys.end(
            "FileNotFoundError: No such file or directory: '%s'" %
            file, __file__, 0
        );
