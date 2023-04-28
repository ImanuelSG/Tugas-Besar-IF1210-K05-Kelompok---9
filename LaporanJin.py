#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Global


def laporanjin():
    pasir = Global.bahan[1][2]
    batu = Global.bahan[2][2]
    air = Global.bahan[3][2]
    tempuser = [["" for i in range (3)] for j in range (103)]
    for i in range (103):
        for j in range (3):
            tempuser[i][j] = Global.users[i][j]
    tempcandi = [["" for i in range (5)] for j in range (101)]
    for i in range (101):
        for j in range (5):
            tempcandi[i][j] = Global.candi[i][j]
    delb = ''
    unique = 0
    jumlahbangun = 0
    totaljinb = 0
    totaljink = 0
    for i in range(3,103):
        if tempuser[i][0] != '' and tempuser[i][2] == "jin_pembangun":
            delb = tempuser[i][0]
            unique += 1
            for j in range(3,103):
                if tempuser[j][0] == delb:
                    tempuser[j][0] = ''             
    if unique > 0:
    
        listbangun = [["" for k in range(unique)],[0 for l in range(unique)]]
        i = 0
        j = 0
        k = 0
        l = 0

        for i in range (103):
            for j in range (3):
                tempuser[i][j] = Global.users[i][j]

        i = 0
        j = 0
        
        for i in range(3,103):
            if tempuser[i][0] != '' and tempuser[i][2] == "jin_pembangun":
                delb = tempuser[i][0]
                listbangun[0][j] = delb
                j += 1
                for k in range(3,103):
                    if tempuser[k][0] == delb:
                        tempuser[k][0] = ''


        for k in range(unique):
            for l in range(1,101):
                if listbangun[0][k] == tempcandi[l][1]:
                    jumlahbangun += 1
            listbangun[1][k] = jumlahbangun
            jumlahbangun = 0
            
        i = 0
        j = 0
        k = 0

        for i in range(unique):
            for j in range(i+1, unique):
                if listbangun[1][i] < listbangun[1][j]:
                    temp1 = listbangun[1][i]
                    listbangun[1][i] = listbangun[1][j]
                    listbangun[1][j] = temp1
                    temp0 = listbangun[0][i]
                    listbangun[0][i] = listbangun[0][j]
                    listbangun[0][j] = temp0
                elif listbangun[1][i] == listbangun[1][j]:
                    if listbangun[0][i] > listbangun[0][j]:
                        temp0 = listbangun[0][i]
                        listbangun[0][i] = listbangun[0][j]
                        listbangun[0][j] = temp0
                        
        terajin = listbangun[0][0]
        termalas = listbangun[0][unique-1]
        
    else:
        terajin = "-"
        termalas = "-"

   
    for k in range(3,103):
        if tempuser[k][2] == "jin_pembangun":
            totaljinb += 1
        elif tempuser[k][2] == "jin_pengumpul":
            totaljink += 1
    totaljin = totaljinb + totaljink

    print("> Total Jin: " + str(totaljin))
    print("> Total Jin Pengumpul: " + str(totaljink))
    print("> Total Jin Pembangun: " + str(totaljinb))
    print("> Jin Terajin: " + str(terajin))
    print("> Jin Termalas: "+ str(termalas))
    print("> Jumlah Pasir: "+ str(pasir) +" unit")
    print("> Jumlah Air: "+ str(air)+" unit")
    print("> Jumlah Batu: "+ str(batu) +" unit")
    return
            


# %%
