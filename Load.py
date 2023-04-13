import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="nama folder yang ingin diload")
args = parser.parse_args()

nama_folder = args.nama_folder
file_path = os.path.join(nama_folder, "main.py") # Nama file dan directorynya
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        konten_file = file.read()
    print(konten_file)
else:
    print("File tidak ditemukan")
