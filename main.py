import Login
import Help
import Exit
Database = ["" for i in range(101)]
# Fungsi untuk membagi file csv menjadi username, password, role
def split_csv(line) :
    semicolon = 1
    for i in range (len(line)) :
        if line[i] == ";" :
            semicolon += 1
    Temp = [ "" for i in range (semicolon)] # Array untuk menyimpan semua data dalam 1 baris (Misal username + password + role)
    idx = 0 # Indeks untuk array Temp
    for i in range (len(line)) :
        if  line[i] == "\n" :
            idx+=1
        elif line[i] != ";":
            Temp[idx] += line[i]
        else :
            idx += 1
    return Temp

# Buka file csv dan melakukan pengisian Database melalui fungsi split_csv
def read_csv(file) :
    with open("user.csv","r") as file : 
        idx = 0
        for line in file :
            Database[idx] = split_csv(line)
            idx += 1
read_csv("user.csv")
keluar = False
while keluar == False :
    command = input(">>> ")
    if command == "login":
        Login.login()
    elif command == "help" :
        Help.help() # Fungsi Help
    elif command == "exit" :
        Exit.exit()
        keluar = True
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