print(f'{str(__file__).replace("/", ".")[1:]} imported')
def parseInt(o):
    try: return o.isdigit();
    except: return False;