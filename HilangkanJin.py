import Global
def isRegisteredJin(user):
    benar = 999
    for i in range(3,103):
        if Global.users[i][0] == user:
                benar = i
                break
    return benar

def HilangkanJin ():
    username = input ("Masukkan username jin : ")
    tanda = isRegisteredJin(username)
    if tanda == 999:
        print ("Tidak ada jin dengan username tersebut")
    else :
        pilihan = input ((f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)?"))
        if pilihan == "Y" or pilihan == "y":
            if Global.users[tanda][2] == "jin_pengumpul":
                Global.jumlahjinpengumpul-=1 
            else : 
                Global.jumlahjinpembangun-=1
            Global.users[tanda][0]=[""] ## hapus data jin
            for i in range (100):
                if Global.candi[i][1] == username:
                    Global.candi[i] =["","","","",""]
                    Global.jumlahcandi -= 1

