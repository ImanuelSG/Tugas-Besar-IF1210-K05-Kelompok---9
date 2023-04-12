# pembuatan fungsi logout

def logout():
    global isLoggedOut
    if not isLoggedOut:
        print("Tidak ada akun yang terdaftar!")
        print("Login terlebih dahulu untuk melakukan logout")
        return
    isLoggedIn = False # ketika isLoggedIn = False maka user keluar dari akun
    print("Anda telah logout dari akun")

isLoggedIn = False

