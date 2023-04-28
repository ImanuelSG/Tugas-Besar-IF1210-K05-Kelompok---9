import Global
# Fungsi mengecek apakah username sudah terdaftar dan mengembalikan posisi indeks dari user (untuk track jenis user)
def isRegistered(user:str)->int:
    benar = 999
    for i in range(1,103):
        if Global.users[i] != "" and Global.users[i][0] == user :
            benar = i
            break
    return benar

# Fungsi untuk melakukan pengecekan ketika login dengan suatu username dan password
def login() :
    global isLoggedIn # Dibuat global agar data telah login tetap tersimpan
    global user # Dibuat global agar data user tetap tersimpan
    global id #keep track id user untuk akses matriks
    if isLoggedIn: # Untuk mengecek apakah sudah melakukan login sebelumnya
        print("Login gagal!")
        print(f"Anda telah login dengan username {user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        return
    isCorrect = False
    while isCorrect == False :
        user = input("Username : ")
        password = input("Password : ")
        id = isRegistered(user)
        if id!=999: #jika username memang ada
            if Global.users[id][1]==password: #jika password benar
                print(f"\nSelamat datang, {user}!")
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                isCorrect = True # Ketika True, akan keluar dari loop untuk meminta username dan password
                isLoggedIn = True # Ketika True, user harus melakukan logout agar isLoggedIn menjadi false lalu dapat melakukan login lagi
            else : #jika password salah
                print ("Password salah!")
        else:#Jika username tidak ada
            print("Username tidak terdaftar!")
isLoggedIn = False
id = "a" # Hanya dummy