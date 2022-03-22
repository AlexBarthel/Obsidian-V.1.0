print(f'{str(__file__).replace("/", ".")[1:]} imported')
def parseFloat(o):
    try: return o.replace('.', '', 1).isdigit();
    except: return False;