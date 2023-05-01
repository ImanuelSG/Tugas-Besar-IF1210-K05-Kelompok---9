# Bagian Import
import Login
from Help import Help
import Exit
import Global
from Ayamberkokok import ayamberkokok
from HancurkanCandi import hancurkancandi
from SummonJin import SummonJin
from HilangkanJin import HilangkanJin
from UbahTipeJin import UbahTipeJin
import Logout
from loadandsave import load,save # Fungsi untuk membagi file csv menjadi username, password, roleimport Ayamberkokok
from BatchBangunKumpul import batchbangun,batchkumpul
from LaporanCandi import laporancandi
from LaporanJin import laporanjin
from JinPembangun import JinPembangun
from JinPengumpul import JinPengumpul

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
    elif command == "help" and LoggedIn==False:
        Help(0)
    elif command == "save" :
        save()
    elif LoggedIn == False :
        print("Silakan menggunakan command 'login' terlebih dahulu")
    else : #Jika Sudah login
        if command == "help" :
            Help(Login.id) # Fungsi Help


        elif command == "summonjin" :
            if Global.users[Login.id][0] == "Bondowoso":
                SummonJin() # Fungsi Summon jin
            else: 
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "hapusjin" :
            if Global.users[Login.id][0] == "Bondowoso":
                HilangkanJin() # Fungsi hilangkan jin
            else :
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "ubahjin" :
            if Global.users[Login.id][0] == "Bondowoso":
                UbahTipeJin() # Fungsi ubah jin
            else :
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "batchkumpul" :
            if Global.users[Login.id][0] == "Bondowoso":
                batchkumpul() # Fungsi batch kumpul
            else :
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "batchbangun":
            if Global.users[Login.id][0] == "Bondowoso":
                batchbangun()
            else :
                print("Tidak memiliki izin untuk menggunakan command ini")
        
        
        elif command == "laporanjin" :
            if Global.users[Login.id][0] == "Bondowoso":
                laporanjin() # Fungsi mengambil laporan jin
            else :
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "laporancandi" :
            if Global.users[Login.id][0] == "Bondowoso":
                laporancandi() # Fungsi melapor candi
            else :
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "ayamberkokok" :
            if Global.users[Login.id][0] == "Roro" :
                ayamberkokok() # Fungsi ayam berkokok
            else: 
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "hancurkancandi" :
            if Global.users[Login.id][0] == "Roro" :
                hancurkancandi() # Fungsi menghancurkan candi 
            else : 
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "bangun" :
            if Global.users[Login.id][2]=="jin_pembangun":
                JinPembangun(Global.users[Login.id][0]) # Fungsi bangun jin
            else:  
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "kumpul" :
            if Global.users[Login.id][2]=="jin_pengumpul":
                JinPengumpul() # Fungsi kumpul jin
            else: 
                print("Tidak memiliki izin untuk menggunakan command ini")


        elif command == "logout" :
            Logout.logout() # Fungsi Logout
            LoggedIn = False
            Login.isLoggedIn = None 


        else :
            print ('Command tidak ditemukan, silahkan run command "help" untuk melihat daftar command yang dapat digunakan')

