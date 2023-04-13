import argparse
import os


def load ():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="nama folder yang ingin diload")
    args = parser.parse_args()
    nama_folder = args.nama_folder
    file_path = os.path.join("save",nama_folder) # Nama file dan directorynya
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            konten_file = file.read()
        print(konten_file)
    else:
        print("File tidak ditemukan")

def save ():
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

