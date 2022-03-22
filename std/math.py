print(f'{str(__file__).replace("/", ".")[1:]} imported')
# import custom libraries
from std import sys
from std import nums
# import python libraries
import math

# round, floor, and ceil
def round(x):
	decimal = str(x).split('.');
	if len(decimal) > 1:
		if int(decimal[1]) >= 5:
			return int(decimal[0]) + 1;
		else: return int(decimal[0]);
	else: return x;
def floor(x):
	decimal = str(x).split('.');
	return decimal[0];
def ceil(x):
	decimal = str(x).split('.');
	return int(decimal[0]) + 1;

# factorial
def factorial(n):
	f = 1;
	for i in range(1,n+1):
		f = f * i;
	return f;

# greatest common denominator (gcd)
def gcd(x, y):
    try:
		# equal to zero?
        if (x == 0): return y;
        if (y == 0): return x;
	    # base case
        if (x == y): return x;
	    # x is greater
        if (x > y):
            try:
                return gcd(x-y, y);
            except RecursionError:
                sys.end(
                    "RecursionError: maximum recursion depth exceeded",
                    __file__, 0
                );
	    # y is greater
        try:
            return gcd(x, y-x);
        except RecursionError:
            sys.end(
                "RecursionError: maximum recursion depth exceeded",
                __file__, 0
            );
	# if all else fails
    except RecursionError:
        sys.end(
            "RecursionError: maximum recursion depth exceeded",
            __file__, 0
        );
# least common multiple (lcm)
def lcm(x, y):
    try: return int((x / gcd(x, y)) * y);
    except RecursionError:
        sys.end(
            "RecursionError: maximum recursion depth exceeded",
            __file__, 0
        );

# add, subtract, multiply, divide, modulus, power
def add(x, y):
	return x + y;
def sub(x, y):
	return x - y;
def mult(x, y):
	return x * y;
def div(x, y):
	return x / y;
def mod(x, y):
	return x % y;
def pow(x, y):
	x0 = 1;
	for i in range(y):
		x0 *= x;
	return x0;

# sqrt, dist, exp, radians, degrees, and sgn
def sqrt(x): # square root
	return math.sqrt(x);
def dist(x1, y1, x2, y2): # distance
	return sqrt(
		pow(x2-x1, 2) + pow(y2-y1, 2)
	);
def exp(x): # exponential
	return pow(nums.e, x);
def radians(x): # radians
	return x * nums.PI / 180;
def degrees(x): # degrees
	return x * (180/nums.PI);
def sgn(x): # sign
	if x > 0: return 1;
	elif x < 0: return -1;
	else: return 0;

# sin, cos, tan
def sin(o, h):
	# return opposite over hypotenuse 
    try: return o/h;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );
def cos(a, h):
	# return adjacent over hypotenuse
    try: return a/h;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );
def tan(o, a):
	# return opposite over adjacent
    try: return o/a;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );

# asin, acos, atan, atan2, and hypot
def asin(h, o): # arc sine
	# return hypotenuse over opposite
    try: return h/o;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );
def acos(h, a): # arc cosine
	# return hypotenuse over adjacent
    try: return h/a;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );
def atan(a, o): # arc tangent
	# return adjacent over opposite
    try: return a/o;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );
def atan2(a, o): # arc tangent 2
	# cases
    if o > 0: return a/o;
    if o < 0 and a >= 0: return a/o + nums.PI;
    if o < 0 and a < 0: return a/o - nums.PI;
    if o == 0 and a > 0: return nums.PI/2;
    if o == 0 and a < 0: return -nums.PI/2;
    if o == 0 and a == 0: return nums.undefined;
    # return adjacent over opposite
    try: return a/o;
    except ZeroDivisionError:
        sys.end(
            "ZeroDivisionError: division by zero",
            __file__, 0
        );
# hypot
def hypot(x, y): # hypotenuse
	return (x*x + y*y);