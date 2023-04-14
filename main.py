# Bagian Import
import Login
import Help
import Exit
import Global
import AyamBerkokok
import HancurkanCandi
import SummonJin
import JinPembangun
import HilangkanJin
import UbahTipeJin
import Logout
from loadandsave import load,save # Fungsi untuk membagi file csv menjadi username, password, roleimport Ayamberkokok

load()

LoggedIn = False
keluar = False
while keluar == False :
    command = input(">>> ")
    if command == "login":
        Login.login()
        LoggedIn = True
        Logout.isLoggedOut = None
    elif command == "exit" :
        Exit.exit()
        keluar = True
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
        if LoggedIn and Login.user == "Bondowoso" :
            SummonJin.SummonJin() # Fungsi Summon jin
        elif Login.user != "Bondowoso" : # Jikalau sudah login dan buka Roro maka tidak boleh menggunakan command ayamberkokok
            print("Tidak memiliki izin untuk menggunakan command ini")
    elif command == "bangun" :
        if LoggedIn and Global.users[Login.id][2]=="jin_pembangun":
            JinPembangun.JinPembangun(Global.users[Login.id][0]) # Fungsi bangun jin
        else: # Jikalau sudah login dan buka Roro maka tidak boleh menggunakan command ayamberkokok  
            print("Tidak memiliki izin untuk menggunakan command ini")
    elif command == "hapusjin" :
        HilangkanJin.HilangkanJin() # Fungsi hilangkan jin
    elif command == "ubahjin" :
        UbahTipeJin.UbahTipeJin() # Fungsi ubah jin
    elif command == "save" :
        save()
    
    '''
    elif command == "kumpul" :
        jinpengumpul() # Fungsi kumpul jin
    elif command == "batchkumpul" :
        batchkumpul() # Fungsi batch kumpul
    elif command == "laporanjin" :
        laporanjin() # Fungsi mengambil laporan jin
    elif command == "laporancandi" :
        laporancandi() # Fungsi melapor candi
) # Fungsi save
'''