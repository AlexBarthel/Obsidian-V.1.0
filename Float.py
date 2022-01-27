def parseFloat(o):
    try: return o.replace('.', '', 1).isdigit();
    except: return False;