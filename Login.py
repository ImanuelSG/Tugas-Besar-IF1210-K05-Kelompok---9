import Global
# Fungsi mengecek apakah username dan password sudah terdaftar
def isRegistered(user, password):
    global benar
    benar = False
    for i in range(1,103):
        if Global.users[i] != "" and Global.users[i][0] == user and Global.users[i][1] == password :
                benar = True
                break
    return benar

# Fungsi untuk melakukan pengecekan ketika login dengan suatu username dan password
def login() :
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
            if any([user == Global.users[i][0] for i in range(1,(len(Global.users))) if Global.users[i] != ""]): # Jika username ada tetapi password salah
                print("Password salah!")
            else: # Username yang dimasukkan tidak terdaftar
                print("Username tidak terdaftar!")

isLoggedIn = False