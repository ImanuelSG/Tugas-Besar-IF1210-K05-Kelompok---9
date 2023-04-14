import Global
from RNG import rng
from Global import read_csv

def getsmallestcandi(list,N):#Function untuk mendapatkan indexterkecil candi yang masi kosong
    i=0
    while list[i][0]!='':
        i+=1
        if i == N:
            break
    return i
def JinPembangun (pembangun):
    pasir = rng()
    batu = rng()
    air = rng()
    if (int(Global.bahan[1][2]) >= pasir and int(Global.bahan[2][2]) >= batu and int(Global.bahan[3][2]) >= air):
        for i in range (1,4):
            temp = int(Global.bahan[i][2])
            tools = [pasir,batu,air]
            temp -= tools[i-1]
            Global.bahan[i][2] = temp
        if Global.jumlahcandi <=100:
            tempat = getsmallestcandi(Global.candi,100)
            Global.candi[tempat]=[tempat,pembangun,pasir,batu,air]
            Global.jumlahcandi+=1
        print ("Candi berhasil dibangun")
        print (f"Sisa candi yang perlu dibangun: {100-Global.jumlahcandi}")
        print (Global.candi)
    else :
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun!")



