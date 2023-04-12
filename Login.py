# Untuk Menyimpan Semua Data (Misal Database [0] = ['username','password','role'])
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
def read_csv() :
    with open("user.csv","r") as file : 
        idx = 0
        for line in file :
            Database[idx] = split_csv(line)
            idx += 1

# Fungsi mengecek apakah username dan password sudah terdaftar
def isRegistered(user, password):
    for i in range(1,(len(Database))):
        # Mengecek bahwa database tidak kosong
        if Database[i] :
            if Database[i][0] == user and Database[i][1] == password:
                return True
        else: # loop akan berhenti ketika menemui list kosong yang menandakan bahwa pengecekan telah selesai
            break
    return False

# Fungsi untuk melakukan pengecekan ketika login dengan suatu username dan password
def login():
    global isLoggedIn # Dibuat global agar data telah login tetap tersimpan
    global user # Dibuat global agar data user tetap tersimpan
    if isLoggedIn: # Untuk mengecek apakah sudah melakukan login sebelumnya
        print("Login gagal!")
        print(f"Anda telah login dengan username {user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        return
    isCorrect = False
    while isCorrect == False :
        user = input("Username : ")
        password = input("Password : ")
        if isRegistered(user, password):
            print(f"Selamat datang, {user}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            isCorrect = True # Ketika True, akan keluar dari loop untuk meminta username dan password
            isLoggedIn = True # Ketika True, user harus melakukan logout agar isLoggedIn menjadi false lalu dapat melakukan login lagi
        else:
            if any([user == Database[i][0] for i in range(1,(len(Database))) if Database[i] != ""]): # Jika username ada tetapi password salah
                print("Password salah!")
            else: # Username yang dimasukkan tidak terdaftar
                print("Username tidak terdaftar!")

isLoggedIn = False
''' keluar = False
while keluar == False :
    command = input(">>> ")
    if command == "login" :
        login()
    else :
        exit() #Fungsi exit
    elif command == "logout" :
        logout() #Fungsi Logout
    elif command == "summonjin" :
        summonjin() #Fungsi Summon jin
    elif command == "hapusjin" :
        hapusjin() #Fungsi hilangkan jin
    elif command == "ubahjin" :
        ubahjin() #Fungsi ubah jin
    elif command == "bangun" :
        jinpembangun() #Fungsi bangun jin
    elif command == "kumpul" :
        jinpengumpul() #Fungsi kumpul jin
    elif command == "batchkumpul" :
        batchkumpul() #Fungsi batch kumpul
    elif command == "laporanjin" :
        laporanjin() #Fungsi mengambil laporan jin
    elif command == "laporancandi" :
        laporancandi() #Fungsi melapor candi
    elif command == "hancurkancandi" :
        hancurkancandi() #Fungsi menghancurkan candi
    elif command == "ayamberkokok" :
        ayamberkokok() #Fungsi ayam berkokok
    elif command == "save" :
        save() #Fungsi save
    elif command == "help" :
        help() #Fungsi help '''
