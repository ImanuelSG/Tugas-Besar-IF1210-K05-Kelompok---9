import Global

# Fungsi untuk menghapus candi dari matriks candi
def remove_IDcandi(candi, IDdiHapus):
    for i in range(len(candi)):
        if candi[i] == IDdiHapus:
            candi[i] = ""
            break
    return candi

# Fungsi untuk menghancurkan candi yang diinginkan
def hancurkancandi() :
    for i in range(len(Global.candi)) :
        IDcandi = input("Masukkan ID Candi: ") # ID candi yang ingin dihancurkan
        if len(Global.candi[i]) == 0 : # Keadaan ketika belum ada candi yang dibangun
            print("Belum ada candi yang dibangun")
            break        
        elif IDcandi == Global.candi[i][0] : # Mengecek id dari array dalam matriks candi
            Konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDcandi} (Y/N)? ")
            if Konfirmasi == "Y" :  # Y artinya setuju untuk dihancurkan
                print("Candi telah berhasil dihancurkan.")
                remove_IDcandi(Global.candi, Global.candi[i])
                break
            elif Konfirmasi == "N" : # N artinya tidak setuju untuk dihancurkan
                print("Tidak jadi dihancurkan.")
                break
            else : # Input bukan Y maupun N
                print("Silakan input antara Y atau N.")
        else : # ID candi tidak ada
            print("Tidak ada candi dengan ID tersebut.")
            break