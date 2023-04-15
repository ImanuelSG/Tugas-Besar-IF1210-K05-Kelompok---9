import Global
from Global import isRegisteredJin

def HilangkanJin ():
    username = input ("Masukkan username jin : ")
    tanda = isRegisteredJin(username)
    if tanda == 999:
        print ("Tidak ada jin dengan username tersebut")
    else :
        pilihan = input ((f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)?"))
        if pilihan == "Y" or pilihan == "y":
            Global.users[tanda]=["","",""] ## hapus data jin
            for i in range (101):
                if Global.candi[i][1] == username:
                    Global.candi[i] =["","","","",""]

