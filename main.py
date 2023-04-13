# Bagian Import
import Ayamberkokok
import Login
import Help
import Exit
import Logout
import Global
from JinPembangun import JinPembangun
from HilangkanJin import HilangkanJin
from SummonJin import SummonJin
from UbahTipeJin import UbahTipeJin
from Global import read_csv
from loadandsave import load

load()
read_csv("user.csv",Global.users)
read_csv("bahan_bangunan.csv",Global.bahan)
read_csv("candi.csv",Global.candi)
# Fungsi untuk membagi file csv menjadi username, password, roleimport Ayamberkokok

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
            Ayamberkokok.ayamberkokok() # Fungsi ayam berkokok
        elif Login.user != "Roro" : # Jikalau sudah login dan buka Roro maka tidak boleh menggunakan command ayamberkokok
            print("Tidak memiliki izin untuk menggunakan command ini")
    elif command == "logout" :
        Logout.logout() # Fungsi Logout
        Login.isLoggedIn = None 
    elif command == "exit" :
        Exit.exit()
        keluar = True
    '''elif command == "summonjin" and :
        summonjin() # Fungsi Summon jin
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
    elif command == "hancurkancandi" :
        hancurkancandi() # Fungsi menghancurkan candi
    elif command == "save" :
        save() # Fungsi save
'''