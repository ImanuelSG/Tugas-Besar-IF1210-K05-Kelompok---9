# Bagian Import
import Login
import Help
import Exit
import Global
import AyamBerkokok
import HancurkanCandi
import SummonJin

from Global import read_csv
read_csv("user.csv",Global.users)
read_csv("bahan_bangunan.csv",Global.bahan)
read_csv("candi.csv",Global.candi)

# Fungsi untuk membagi file csv menjadi username, password, roleimport Ayamberkokok
import Logout

LoggedIn = False
keluar = False
while keluar == False :
    command = input(">>> ")
    if command == "login":
        Login.login()
        LoggedIn = True
        Logout.isLoggedOut = None
    elif LoggedIn == False :
        print("Silakan menggunakan command 'login' terlebih dahulu")
    elif command == "help" :
        if LoggedIn :
            Help.help() # Fungsi Help
        else : # Belum login
            print("Silakan menggunakan command 'login' terlebih dahulu")
    elif command == "ayamberkokok" :
        if LoggedIn and Login.user == "Roro" :
            AyamBerkokok.ayamberkokok() # Fungsi ayam berkokok
        elif Login.user != "Roro" : # Jikalau sudah login dan buka Roro maka tidak boleh menggunakan command ayamberkokok
            print("Tidak memiliki izin untuk menggunakan command ini")
    elif command == "logout" :
        Logout.logout() # Fungsi Logout
        Login.isLoggedIn = None 
    elif command == "hancurkancandi" :
        if LoggedIn and Login.user == "Roro" :
            HancurkanCandi.hancurkancandi() # Fungsi menghancurkan candi 
        elif Login.user != "Roro" : # Jikalau sudah login dan buka Roro maka tidak boleh menggunakan command ayamberkokok
            print("Tidak memiliki izin untuk menggunakan command ini")
    elif command == "summonjin" :
        SummonJin.SummonJin() # Fungsi Summon jin
    elif command == "exit" :
        Exit.exit()
        keluar = True

    '''
    elif command == "hapusjin" :
        hapusjin() # Fungsi hilangkan jin
    elif command == "ubahjin" :
        ubahjin() # Fungsi ubah jin
    elif command == "bangun" :
        jinpembangun() # Fungsi bangun jin
    elif command == "kumpul" :
        jinpengumpul() # Fungsi kumpul jin
    elif command == "batchkumpul" :
        batchkumpul() # Fungsi batch kumpul
    elif command == "laporanjin" :
        laporanjin() # Fungsi mengambil laporan jin
    elif command == "laporancandi" :
        laporancandi() # Fungsi melapor candi
    elif command == "save" :
        save() # Fungsi save
'''