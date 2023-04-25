import Global
from Global import getsmallestindex,getbiggestindex
def undo ():
    for i in range (3):#mengembalikan jin ke list user
        Global.users[getsmallestindex(Global.users,102)][i] = Global.userundo[i]
    for i in range (getbiggestindex(Global.candiundo,100)+1):
        tempat = getsmallestindex(Global.candi, 100)
        for j in range (5):
            Global.candi[tempat][j]=Global.candiundo[i][j]