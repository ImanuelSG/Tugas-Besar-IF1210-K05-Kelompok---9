#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Global
from Global import read_csv


def laporanjin():
    pasir = Global.bahan[1][2]
    batu = Global.bahan[2][2]
    air = Global.bahan[3][2]
    tempuser = Global.users
    tempcandi = Global.candi
    delb = ""
    unique = 0
    jumlahbangun = 0
    totaljinb = 0
    totaljink = 0
    
    if user != Global.user[1][0]:
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        for i in range(1,101):
            if tempcandi[i][1] != "":
                delb = tempcandi[i][1]
                unique += 1
                for j in range(i,101):
                    if tempcandi[i][1] == delb:
                        tempcandi[i][1] = ""
                        
        if unique > 0:
        
            listbangun = [["" for k in range(unique)],[0 for l in range(unique)]]
            tempcandi = Global.candi
            i = 0
            j = 0
            k = 0
            l = 0

            for j in range(1,101):
                if tempcandi[j][1] != "":
                    delb = tempcandi[j][1]
                    listbangun[0][i] = delb
                    i += 1
                    for j in range(j,101):
                    if tempcandi[j][1] == delb:
                        tempcandi[j][1] = ""

            tempcandi = Global.candi

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
            
        tempcandi = Global.candi
        
        for k in range(3,103):
            if tempuser[k][2] == Jin_Pembangun
                totaljinb += 1
            elif tempuser[k][2] == Jin_Pengumpul
                totaljink += 1
        totaljin = totaljinb + totaljink

        
        
        print("> Total Jin: " + str(totaljin))
        print("> Total Jin Pengumpul: " + str(totaljink))
        print("> Total Jin Pembangun: " + str(totaljinb))
        print("> Jin Terajin: " + str(terajin))
        print("> Jin Termalas: "+ str(termalas))
        print("> Jumlah Pasir: "+ pasir +" unit")
        print("> Jumlah Air: "+ air +" unit")
        print("> Jumlah Batu: "+ batu +" unit")
        
                    
            

