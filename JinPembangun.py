import Global
import random
def getsmallestcandi(list,N):#Function untuk mendapatkan indexterkecil candi yang masi kosong
    i=0
    while list[i]!=['','','','','']:
        i+=1
        if i == N:
            break
    return i
def JinPembangun (pembangun):
    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
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
    else :
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun!")




