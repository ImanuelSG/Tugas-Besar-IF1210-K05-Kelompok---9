#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Global


def laporancandi():
    tempcandi = [["" for i in range (5)] for j in range (101)]
    for i in range (101):
        for j in range (5):
            tempcandi[i][j] = Global.candi[i][j]
    totalcandi = 0
    totalpasir = 0
    totalbatu = 0
    totalair = 0

    for i in range(1,101):
        if tempcandi[i][0] != "":
            totalcandi += 1
            
    if totalcandi == 0:
        print("> Total Candi: 0")
        print("> Total Pasir yang digunakan: 0")
        print("> Total Batu yang digunakan: 0")
        print("> Total Air yang digunakan: 0")
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")

    else:
        datacandi = [["" for i in range(totalcandi)],[0 for i in range(totalcandi)]] ## id , harga
        
        j = 0
        for k in range(1,101):
            if tempcandi[k][0] != "":
                tempid = tempcandi[k][0]
                tempcandi[k][0] = ""
                datacandi[0][j] = tempid
                pasir = int(Global.candi[k][2])
                batu = int(Global.candi[k][3])
                air = int(Global.candi[k][4])
                totalpasir += pasir
                totalbatu += batu
                totalair += air
                harga = 10000 * pasir + 15000 * batu + 7500 * air
                datacandi[1][j] = harga
                j += 1
                
        i = 0
        j = 0
        k = 0

        for i in range(totalcandi):
            for j in range(i+1, totalcandi):
                if datacandi[1][i] < datacandi[1][j]:
                    temp1 = datacandi[1][i]
                    datacandi[1][i] = datacandi[1][j]
                    datacandi[1][j] = temp1
                    temp0 = datacandi[0][i]
                    datacandi[0][i] = datacandi[0][j]
                    datacandi[0][j] = temp0
        termahal = datacandi[0][0]
        hargamah = datacandi[1][0]
        termurah = datacandi[0][totalcandi-1]
        hargamur = datacandi[1][totalcandi-1]
        print("> Total Candi: " + str(totalcandi))
        print("> Total Pasir yang digunakan: " + str(totalpasir))
        print("> Total Batu yang digunakan: " + str(totalbatu))
        print("> Total Air yang digunakan: " + str(totalair))
        print("> ID Candi Termahal: "+ str(termahal) +" (Rp "+ str(hargamah) +")")
        print("> ID Candi Termurah: "+ str(termurah) +" (Rp "+ str(hargamur)+")")

