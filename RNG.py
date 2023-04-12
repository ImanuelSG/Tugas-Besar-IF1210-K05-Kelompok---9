import datetime

def rng():
    time = datetime.datetime.now()
    h = time.hour
    m = time.minute
    s = time.second
    seed = h*24 + m*60 + s
    num = 0
    lcg = (seed * 134775813 + 1013904223) % 2**16
    if 0 <= lcg <= 10922:
        num = 0
    elif 10923 <= lcg <= 21845:
        num = 1
    elif 21846 <= lcg <= 32768:
        num = 2
    elif 32769 <= lcg <= 43691:
        num = 3
    elif 43692 <= lcg <= 54615:
        num = 4
    elif 54616 <= lcg <= 65536:
        num = 5
    return num

print(rng())
