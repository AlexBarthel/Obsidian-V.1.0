def parseString(o):
    try: return (o[0] == '"' and o[-1] == '"') or (o[0] == "'" and o[-1] == "'");
    except: return False;