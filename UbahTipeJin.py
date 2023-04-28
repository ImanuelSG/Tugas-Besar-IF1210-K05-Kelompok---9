import Global
import HilangkanJin
from Global import isRegisteredJin

def UbahTipeJin():
    username = input("Masukkan username jin : ")
    posisi = isRegisteredJin(username)
    if isRegisteredJin(username) == 999:
        print ("Tidak ada jin dengan username tersebut.")
    else :
        if Global.users[posisi][2] == "jin_pengumpul":
            show = ["Pengumpul","Pembangun"]
        else :
            show = ["Pembangun","Pengumpul"]
        pilihan = str (input(f'Jin ini bertipe "{show[0]}". Yakin ingin mengubah ke tipe "{show[1]}" (Y/N)? '))
        if pilihan == 'Y' or pilihan == 'y':
            if Global.users[posisi][2] == 'jin_pengumpul':
                Global.users[posisi][2] = 'jin_pembangun'
            else :
                Global.users[posisi][2] = 'jin_pengumpul'
            print ("Jin telah berhasil diubah.")
