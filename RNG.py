import datetime
time = datetime.datetime.now()

y = time.year
mn = time.month
d = time.day
h = time.hour
m = time.minute
s = time.second
seed =(y*365 + mn*30 + d)*24*60 + h*24 + m*60 + s
def rng(): #rng untuk mengumpul
    global seed
    num = 0
    seed = (seed * 134775813 + 1013904223) % 2**16
    if 0 <= seed <= 10922:
        num = 0
    elif 10923 <= seed <= 21845:
        num = 1
    elif 21846 <= seed <= 32768:
        num = 2
    elif 32769 <= seed <= 43691:
        num = 3
    elif 43692 <= seed <= 54615:
        num = 4
    elif 54616 <= seed <= 65536:
        num = 5
    return num

def rngb(): #rng untuk membangun
    global seed
    num = 0
    seed = (seed * 134775813 + 1013904223) % 2**16
    if 0 <= seed <= 13107:
        num = 1
    elif 13108 <= seed <= 26215:
        num = 2
    elif 26216 <= seed <= 39323:
        num = 3
    elif 39324 <= seed <= 52430:
        num = 4
    elif 52431 <= seed <= 65536:
        num = 5
    return num
