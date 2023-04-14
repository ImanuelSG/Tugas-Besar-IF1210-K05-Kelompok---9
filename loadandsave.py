import argparse
import os
import Global
from Global import read_csv

# Fungsi untuk melakukan load
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="Nama Folder yang akan di load" ,nargs='?')
    args = parser.parse_args()
    nama_folder = args.nama_folder
    if nama_folder is None:
        print("\n")
        print("Tidak ada nama folder yang diberikan!")
        print ("\n")
        print ("Usage: python main.py <nama_folder>")
        quit()
    else: 
        file_path = os.path.join("save",nama_folder) # Nama file dan directorynya
        if os.path.exists(file_path):
            print ("\n")
            print ("Loading...")
            print ("\n")
            print ('Selamat datang di program "Manajerial Candi"')
            print ("Silahkan masukkan username Anda")
            read_csv(os.path.join(file_path,"bahan_bangunan.csv"), Global.bahan)
            read_csv(os.path.join(file_path,"user.csv"), Global.users)
            read_csv(os.path.join(file_path,"candi.csv"), Global.candi)
        else :
            print ("\n")
            print (f'Folder "{nama_folder}" tidak ditemukan.')
            quit()

# Fungsi untuk melakukan save
def save():
    global fulldir
    mainfolder_name = "save"
    subfolder_name = str (input("Masukkan nama folder: "))
    fulldir = os.path.join(mainfolder_name, subfolder_name)
    if not os.path.exists(mainfolder_name):
        os.makedirs(fulldir)
        
    elif not os.path.exists(fulldir):
        os.makedirs(fulldir)
    else:
        print ("Sudah ada")

