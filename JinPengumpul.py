#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import Global
from RNG import rng

def JinPengumpul():
    #if Global.users[id][2]  != Jin_Pembangun
        #-Put Something here to deny access-
    #else (suatu kyk gini perlu ga?)
    pasir = rng()
    batu = rng()
    air = rng()
    print("Jin menemukan " + str(pasir) + " pasir, " + str(batu) + " batu, dan " + str(air) + " air.")
    for i in range (1,4):
        temp = int(Global.bahan[i][2])
        tools = [pasir,batu,air]
        temp += tools[i-1]
        Global.bahan[i][2] = temp
# %%
