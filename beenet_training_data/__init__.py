#All hail the BDFL

def datapath():
    i = __file__.rfind("/")
    return __file__[:i+1]
