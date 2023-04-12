import Global
from SummonJin import SummonJin
import HilangkanJin
from Global import read_csv
def isRegisteredJin(user):
    benar = 999
    for i in range(3,103):
        if Global.users[i][0] == user:
                benar = i
                break
    return benar
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
        if pilihan == 'Y':
            if Global.users[posisi][2] == 'jin_pengumpul':
                Global.users[posisi][2] = 'jin_pembangun'
                Global.jumlahjinpembangun+=1
                Global.jumlahjinpengumpul-=1
                print ("a")
            else :
                Global.users[posisi][2] = 'jin_pengumpul'
                Global.jumlahjinpembangun-=1
                Global.jumlahjinpengumpul+=1
                print ("b")
read_csv("user.csv",Global.users)
read_csv("bahan_bangunan.csv",Global.bahan)
read_csv("candi.csv",Global.candi)
while True:
    SummonJin()
    UbahTipeJin()
    print (Global.users)
