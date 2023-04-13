import argparse
import os


def load ():
    parser = argparse.ArgumentParser()
    parser.add_argument()

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

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="nama folder yang ingin diload") # Tulis nama file lalu tulis nama folder utk load (buat d sni)
args = parser.parse_args()

# Cara akses
nama_folder = args.nama_folder

# Cek file ada atau tidak
if os.path.exists(nama_folder):
    # Konten file dibaca
    with open(nama_folder, "r") as file:
        konten_file = file.read()
    print(konten_file)
else:
    print("File tidak ditemukan")