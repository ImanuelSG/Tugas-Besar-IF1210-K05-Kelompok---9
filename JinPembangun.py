import Global
from RNG import rngb

def getsmallestcandi(list:list)->int:#Function untuk mendapatkan indexterkecil candi yang masi kosong
    i=0
    while list[i][0]!='':
        i+=1
        if i == 100:
            break
    return i
    
def getjumlahcandi(list:list)->int:#Function untuk mendapatkan jumlahcandi yang sudah dibangun
    count=0
    for i in range (1,101):
        if list[i][0]!='':
            count+=1
    return count

def JinPembangun (pembangun):
    pasir = rngb()
    batu = rngb()
    air = rngb()
    if (int(Global.bahan[1][2]) >= pasir and int(Global.bahan[2][2]) >= batu and int(Global.bahan[3][2]) >= air):
        for i in range (1,4):
            temp = int(Global.bahan[i][2])
            tools = [pasir,batu,air]
            temp -= tools[i-1]
            Global.bahan[i][2] = temp
        if getjumlahcandi(Global.candi) <100:
            tempat = getsmallestcandi(Global.candi)
            Global.candi[tempat]=[tempat,pembangun,pasir,batu,air]
        print ("Candi berhasil dibangun")
        print (f"Sisa candi yang perlu dibangun: {100-getjumlahcandi(Global.candi)}")
    else :
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun!")


