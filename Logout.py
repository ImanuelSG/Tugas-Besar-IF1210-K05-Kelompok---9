# Fungsi Logout
def logout():
    global isLoggedOut
    if isLoggedOut == True : # User belum melakukan login
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else : # User akan melakukan logout
        print("Anda telah logout dari akun")    
    isLoggedOut = True # Ketika isLoggedOut = False maka user keluar dari akun

isLoggedOut = False # Inisialisasi bahwa belum terjadinya logout

