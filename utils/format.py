# import custom libraries
from std import sys

def format(file):
    global content;
    content = [];
    # open the file
    try:
        with open(file, 'r') as f:
            content.append(f.readlines());
        content = content[0];

        for lineno in range(0, len(content)):
            if (len(content[lineno])) > 2:
                content[lineno] = content[lineno].strip('\n');
        return content
    except FileNotFoundError:
		# give the function a chance to return an error before returning.
        sys.end(
            "FileNotFoundError: No such file or directory: '%s'" %
            file, __file__, 0
        );
    return content;
