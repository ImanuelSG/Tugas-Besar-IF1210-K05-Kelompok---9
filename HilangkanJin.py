import Global
from Global import isRegisteredJin,getsmallestindex

def HilangkanJin ():
    username = input ("Masukkan username jin : ")
    tanda = isRegisteredJin(username)
    if tanda == 999:
        print ("Tidak ada jin dengan username tersebut")
    else :
        pilihan = input ((f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)?"))
        if pilihan == "Y" or pilihan == "y":
            Global.userundo=[Global.users[tanda][0],Global.users[tanda][1],Global.users[tanda][2]]
            Global.users[tanda]=["","",""] ## hapus data jin
            for i in range (101):
                if Global.candi[i][1] == username:
                    Global.candiundo[getsmallestindex(Global.candiundo, 102)]=[Global.candi[i][0],Global.candi[i][1],Global.candi[i][2],Global.candi[i][3],Global.candi[i][4]]
                    Global.candi[i] =["","","","",""]
