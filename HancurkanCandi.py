import Global


# Fungsi untuk menghapus candi dari matriks candi
def remove_IDcandi(candi, IDdiHapus):
    for i in range(len(candi)):
        if candi[i] == IDdiHapus:
            candi[i] = ""
            break
    return candi

def isRegisteredCandi(IDcandi) :
    benar = False
    for i in range(100) :
        if Global.candi[i][0] == IDcandi :
            benar = True
    return benar

# Fungsi untuk menghancurkan candi yang diinginkan
def hancurkancandi() :
    IDcandi = input("Masukkan ID Candi: ") # ID candi yang ingin dihancurkan   
    if isRegisteredCandi(IDcandi) : # Mengecek id dari array dalam matriks candi
        Konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDcandi} (Y/N)? ")
        if Konfirmasi == "Y" :  # Y artinya setuju untuk dihancurkan
            print("Candi telah berhasil dihancurkan.")
            remove_IDcandi(Global.candi, Global.candi[IDcandi])
        elif Konfirmasi == "N" : # N artinya tidak setuju untuk dihancurkan
            print("Tidak jadi dihancurkan.")
        else : # Input bukan Y maupun N
            print("Silakan input antara Y atau N.")
    else : # ID candi tidak ada
        print("Tidak ada candi dengan ID tersebut.")
        print(IDcandi)

