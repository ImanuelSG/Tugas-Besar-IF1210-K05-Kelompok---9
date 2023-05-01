# Fungsi untuk help
import Global
def Help(id) :
    if id == 0 :#Belum Login
        print("Daftar command yang dapat dipakai adalah:")
        print("1. login \nUntuk masuk menggunakan akun")
        print("2. exit \nUntuk keluar dari program dan kembali ke terminal")
    else :#Sudah Login
        if Global.users[id][0] == "Bondowoso":#Jika username == Bondowoso
            print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin \nUntuk memanggil jin")
            print("3. hapusjin \nUntuk menghilangkan jin")
            print("4. ubahjin \nUntuk mengubah tipe jin")
            print("5. batchkumpul \nUntuk mengerahkan jin untuk mengumpulkan bahan")
            print("6. laporanjin \nUntuk menampilkan informasi mengenai bahan dan jin")
            print("7. laporancandi \nUntuk menampilkan banyak candi dan bahan yang digunakan")
            print("8. save \nUntuk menyimpan data")
            print("9. exit \nUntuk keluar dari program dan kembali ke terminal")
        elif Global.users[id][0] == "Roro" :#Jika username == Roro
            print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi \nUntuk menghancurkan candi")
            print("3. ayamberkokok \nUntuk memalsukan pagi hari")
            print("4. save \nUntuk menyimpan data")
            print("5. exit \nUntuk keluar dari program dan kembali ke terminal")
        elif Global.users[id][2] == "jin_pembangun": #Jika username == Jin
            print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
            print("2. bangun \nUntuk membangun candi")
            print("3. save \nUntuk menyimpan data")
            print("4. exit \nUntuk keluar dari program dan kembali ke terminal")
        elif Global.users[id][2] == "jin_pengumpul":
            print("1. logout \nUntuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul \nUntuk mengumpulkan bahan")
            print("3. save \nUntuk menyimpan data")
            print("4. exit \nUntuk keluar dari program dan kembali ke terminal")
