import Global 
def rng(): #rng untuk mengumpul
    num = 0
    Global.seed = (Global.seed * 134775813 + 1013904223) % 2**16
    if 0 <= Global.seed <= 10922:
        num = 0
    elif 10923 <= Global.seed <= 21845:
        num = 1
    elif 21846 <= Global.seed <= 32768:
        num = 2
    elif 32769 <= Global.seed <= 43691:
        num = 3
    elif 43692 <= Global.seed <= 54615:
        num = 4
    elif 54616 <= Global.seed <= 65536:
        num = 5
    return num

def rngb(): #rng untuk membangun
    num = 0
    Global.seed = (Global.seed * 134775813 + 1013904223) % 2**16
    if 0 <= Global.seed <= 13107:
        num = 1
    elif 13108 <= Global.seed <= 26215:
        num = 2
    elif 26216 <= Global.seed <= 39323:
        num = 3
    elif 39324 <= Global.seed <= 52430:
        num = 4
    elif 52431 <= Global.seed <= 65536:
        num = 5
    return num
