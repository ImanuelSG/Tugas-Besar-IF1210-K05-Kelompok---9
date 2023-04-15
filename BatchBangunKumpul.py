#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Global
from RNG import rng
from RNG import rngb
from Global import read_csv

import JinPembangun
import JinPengumpul
from JinPembangun import getsmallestcandi
from JinPengumpul import kumpul

def batchkumpul():
    tempuser = Global.users
    totaljin = 0
    totalbahan = 0
    pasir = 0
    batu = 0
    air = 0
    
    for i in range(3,103):
        if tempuser[i][2] == Jin_Pengumpul
            totaljin += 1
    if totaljin = 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print("Mengerahkan " + str(totaljin) + " jin untuk mengumpulkan bahan.")
        for j in range(totaljin):
            pasir += rng()
            batu += rng()
            air += rng()
        
        for k in range(1,4):
        temp = int(Global.bahan[i][2])
        tools = [pasir,batu,air]
        temp += tools[k-1]
        Global.bahan[k][2] = temp
        
        print("Jin menemukan total" + str(pasir) + "pasir, " + str(batu) + " batu, dan " + str(air) + " air.")

        
def batchbangun():
    tempcandi = Global.candi
    tempjcandi = Global.jumlahcandi
    tempuser = Global.users
    totaljin = 0
    totalbahan = [0 for i in range(3)]
    pasir = 0
    batu = 0
    air = 0
    latestid = 0
    
    for i in range(3,103):
        if tempuser[i][2] == Jin_Pembangun
            totaljin += 1
            
    if totaljin = 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        
        for j in range(totaljin):
            for k in range(3,103):
                if tempuser[k][2] == Jin_Pembangun and k > latestid:
                    pembangun = tempuser[k][0]
                    latestid = k
                    break
                    
            pasir = rngb()
            batu = rngb()
            air = rngb()
            totalbahan[0] += pasir
            totalbahan[1] += batu
            totalbahan[2] += air
            if tempjcandi <= 100:
                tempat = getsmallestcandi(Global.candi,100)
                tempcandi[tempat]=[tempat,pembangun,pasir,batu,air]
                tempjcandi+=1
                
        print("Mengerahkan "+ str(totaljin) +" jin untuk membangun candi dengan total bahan "+ str(totalbahan[0]) +" pasir, "+ str(totalbahan[1]) +" batu, dan "+ str(totalbahan[2]) +" air.")
        
        if (int(Global.bahan[1][2]) >= totalbahan[0] and int(Global.bahan[2][2]) >= totalbahan[1] and int(Global.bahan[3][2]) >= totalbahan[2]): 
            Global.candi = tempcandi
            Global.jumlahcandi = tempjcandi
            print("Jin berhasil membangun total "+ str(totaljin) +" candi.")
        else:
            print("Bangun gagal. Kurang "+ str(totalbahan[0] - Global.bahan[1][2]) +" pasir, "+ str(totalbahan[1] - Global.bahan[2][2]) +" batu, dan "+ str(totalbahan[2] - Global.bahan[3][2]) +" air.")

