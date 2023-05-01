#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Global
from RNG import rng
from RNG import rngb

import JinPembangun
import JinPengumpul
from JinPembangun import getsmallestcandi
from JinPengumpul import JinPengumpul
from JinPembangun import getjumlahcandi
def batchkumpul():
    tempuser = Global.users
    totaljin = 0
    totalbahan = 0
    pasir = 0
    batu = 0
    air = 0

    for i in range(3,103):
        if tempuser[i][2] == "jin_pengumpul":
            totaljin += 1

    if totaljin == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print("Mengerahkan " + str(totaljin) + " jin untuk mengumpulkan bahan.")
        for j in range(totaljin):
            pasir += rng()
            batu += rng()
            air += rng()
        for k in range(1,4):
            temp = int(Global.bahan[k][2])
            tools = [pasir,batu,air]
            temp += tools[k-1]
            Global.bahan[k][2] = temp
        
        print("Jin menemukan total " + str(pasir) + "pasir, " + str(batu) + " batu, dan " + str(air) + " air.")

        
def batchbangun():
    tempcandi = [["" for i in range (5)] for j in range (101)]
    for i in range (101):
        for j in range (5):
            tempcandi[i][j] = Global.candi[i][j]
    tempjcandi=getjumlahcandi(Global.candi)
    tempuser = Global.users
    totaljin = 0
    totalbahan = [0 for i in range(3)]
    pasir = 0
    batu = 0
    air = 0
    latestid = 0
    
    for i in range(3,103):
        if tempuser[i][2] == "jin_pembangun":
            totaljin += 1
            
    if totaljin == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        
        for j in range(totaljin):
            for k in range(3,103):
                if tempuser[k][2] == "jin_pembangun" and k > latestid:
                    pembangun = tempuser[k][0]
                    latestid = k
                    break
                    
            pasir = rngb()
            batu = rngb()
            air = rngb()
            totalbahan[0] += pasir
            totalbahan[1] += batu
            totalbahan[2] += air
            if tempjcandi < 100:
                tempat = getsmallestcandi(tempcandi)
                tempcandi[tempat]=[tempat,pembangun,pasir,batu,air]
                tempjcandi+=1

    
                
        print("Mengerahkan "+ str(totaljin) +" jin untuk membangun candi dengan total bahan "+ str(totalbahan[0]) +" pasir, "+ str(totalbahan[1]) +" batu, dan "+ str(totalbahan[2]) +" air.")
        
        if (int(Global.bahan[1][2]) >= totalbahan[0] and int(Global.bahan[2][2]) >= totalbahan[1] and int(Global.bahan[3][2]) >= totalbahan[2]):
            for i in range (101):
                for j in range (5):
                    Global.candi[i][j]=tempcandi[i][j] 
            for i in range (1,4):
                Global.bahan[i][2] -= totalbahan[i-1]
            print("Jin berhasil membangun total "+ str(totaljin) +" candi.")
        else:
            if Global.bahan[1][2] < totalbahan[0]: # Hanya pasir yang Kurang
                if Global.bahan[2][2] < totalbahan [1]: # pasir dan batu kurang
                    if Global.bahan[3][2] <totalbahan[2]:# Ketiganya kurang
                        print("Bangun gagal. Kurang "+ str(totalbahan[0] - Global.bahan[1][2]) +" pasir, "+ str(totalbahan[1] - Global.bahan[2][2]) +" batu, dan "+ str(totalbahan[2] - Global.bahan[3][2]) +" air.")
                    else:
                        print("Bangun gagal. Kurang "+ str(totalbahan[0] - Global.bahan[1][2]) +" pasir dan "+ str(totalbahan[1] - Global.bahan[2][2]) +" batu.")
                elif Global.bahan[3][2] < totalbahan[2]: #pasir dan air kurang
                    print ("Bangun gagal. Kurang " + str(totalbahan[0] - Global.bahan[1][2]) +" pasir dan "+ str (totalbahan[2]-Global.bahan[3][2]) +" air.")
                else:
                    print("Bangun gagal. Kurang "+ str(totalbahan[0] - Global.bahan[1][2]) +" pasir.")
            elif Global.bahan[2][2] <totalbahan[1]: # Hanya batu kurang
                if Global.bahan[3][2] < totalbahan[2]: # batu dan air kurang
                    print ("Bangun gagal. Kurang "+ str(totalbahan[1] - Global.bahan[2][2]) +" batu dan "+ str(totalbahan[2] - Global.bahan[3][2]) +" air.")
                else:
                    print ("Bangun gagal. Kurang "+ str(totalbahan[1] - Global.bahan[2][2]) +" batu.")
            else: # air kurang
                print("Bangun gagal. Kurang "+ str(totalbahan[2] - Global.bahan[3][2]) +" air.")
                