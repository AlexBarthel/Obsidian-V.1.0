print(f'{str(__file__).replace("/", ".")[1:]} imported')
def parseBoolean(o):
    return str(o) == 'true' or str(o) == 'false';