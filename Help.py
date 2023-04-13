# Fungsi untuk help
import Login
def help() :
    if Login.isLoggedIn == False :
        print("Daftar command yang dapat dipakai adalah:")
        print("1. login \nUntuk masuk menggunakan akun")
        print("2. exit \nUntuk keluar dari program dan kembali ke terminal")
    elif Login.isLoggedIn == True and Login.user == "Bondowoso" :
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin \nUntuk memanggil jin")
        print("3. hapusjin \nUntuk menghilangkan jin")
        print("4. ubahjin \nUntuk mengubah tipe jin")
        print("5. batchkumpul \nUntuk mengerahkan jin untuk mengumpulkan bahan")
        print("6. laporanjin \nUntuk menampilkan informasi mengenai bahan dan jin")
        print("7. laporancandi \nUntuk menampilkan banyak candi dan bahan yang digunakan")
        print("8. save \nUntuk menyimpan data")
        print("9. exit \nUntuk keluar dari program dan kembali ke terminal")
    elif Login.isLoggedIn == True and Login.user == "Roro" :
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi \nUntuk menghancurkan candi")
        print("3. ayamberkokok \nUntuk memalsukan pagi hari")
        print("4. save \nUntuk menyimpan data")
        print("5. exit \nUntuk keluar dari program dan kembali ke terminal")
    else : # Jin
        print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
        print("2. bangun \nUntuk membangun candi")
        print("3. kumpul \nUntuk mengumpulkan bahan")
        print("4. exit \nUntuk keluar dari program dan kembali ke terminal")

help ()