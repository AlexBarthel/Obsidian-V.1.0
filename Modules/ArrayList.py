print(f'{str(__file__).replace("/", ".")[1:]} imported')
def parseArrayList(o):
    try: return o[0] == '[' and o[-1] == ']';
    except: return False;