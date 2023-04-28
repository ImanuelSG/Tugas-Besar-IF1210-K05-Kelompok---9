import Global
import typing
from loadandsave import load
from Global import getbiggestindex
# Fungsi untuk menghapus candi dari matriks candi
def remove_IDcandi(candi:int, IDdiHapus:int) -> list:
    for i in range(getbiggestindex(candi,100)+1):
        if candi[i][0] == IDdiHapus:
            candi[i] = ['','','','','']
            break
    return candi

# Fungsi untuk mengecek apakah ID dari candi yang dimasukkan ada atau tidak
def isRegisteredCandi(IDcandi:int)  -> int:
    benar = 999
    for i in range(1,101) :
        if Global.candi[i][0] == IDcandi :
            benar = i
    return benar

# Fungsi untuk menghancurkan candi yang diinginkan
def hancurkancandi() :
    IDcandi = int(input("Masukkan ID Candi: ")) # ID candi yang ingin dihancurkan   
    if isRegisteredCandi(IDcandi) !=999: # Mengecek id dari array dalam matriks candi
        Konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDcandi} (Y/N)? ")
        if Konfirmasi == "Y" :  # Y artinya setuju untuk dihancurkan
            print("Candi telah berhasil dihancurkan.")
            remove_IDcandi(Global.candi, IDcandi)
        elif Konfirmasi == "N" : # N artinya tidak setuju untuk dihancurkan
            print("Tidak jadi dihancurkan.")
        else : # Input bukan Y maupun N
            print("Silakan input antara Y atau N.")
    else : # ID candi tidak ada
        print("Tidak ada candi dengan ID tersebut.")
