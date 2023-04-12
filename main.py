import Login
import Help

keluar = False
while not keluar:
    command = input(">>> ")
    if command == "login":
        Login.login()
    elif command == "help":
        Help.help() # Fungsi Help
    '''elif command == "logout" :
        logout() # Fungsi Logout
    elif command == "summonjin" :
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
    elif command == "ayamberkokok" :
        ayamberkokok() # Fungsi ayam berkokok
    elif command == "save" :
        save() # Fungsi save
'''