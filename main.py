# Bagian Import
import Login
import Help
import Exit
import Ayamberkokok
import Logout

keluar = False
while keluar == False :
    command = input(">>> ")
    if command == "login":
        Login.login()
    elif command == "help" :
        Help.help() # Fungsi Help
    elif command == "ayamberkokok" :
        Ayamberkokok.ayamberkokok() # Fungsi ayam berkokok
    elif command == "logout" :
        Logout.logout() # Fungsi Logout
    elif command == "exit" :
        Exit.exit()
        keluar = True

    '''elif command == "summonjin" :
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