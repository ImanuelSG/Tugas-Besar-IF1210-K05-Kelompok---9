import argparse
import os
import Global
from Global import read_csv,getbiggestindex,read_csv_candi,read_csv_bahan

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
            read_csv_bahan(os.path.join(file_path,"bahan_bangunan.csv"), Global.bahan)
            read_csv(os.path.join(file_path,"user.csv"), Global.users)
            read_csv_candi(os.path.join(file_path,"candi.csv"), Global.candi)
        else :
            print ("\n")
            print (f'Folder "{nama_folder}" tidak ditemukan.')
            quit()

def matrixtocsvril(matrix, filename,N,k):
    with open(filename, "w") as file:
        iteration = Global.getbiggestindex(matrix, N)
        for i in range(iteration+1):
            row_str = ""
            if matrix[i][0]!= "":
                for j in range(k):
                    if j == 0:
                        row_str += str(matrix[i][j])
                    else:
                        row_str += ";" + str(matrix[i][j])
                if i!=iteration:
                    file.write(row_str + "\n")
                else:
                    file.write(row_str)

def save ():
    mainfolder_name = "save"
    subfolder_name = str (input("Masukkan nama folder: "))
    fulldir = os.path.join(mainfolder_name, subfolder_name)
    fulldir=fulldir.replace('\\','/')
    if not os.path.exists(mainfolder_name):
        os.makedirs(fulldir)
        print ("\n")
        print ("Saving...")
        print ("\n")
        print (f"Membuat folder {mainfolder_name}...")
        print (f"Membuat folder {fulldir}...")
        print ("\n")
        print (f"Berhasil menyimpan data di folder {fulldir}!")
    elif not os.path.exists(fulldir):
        os.makedirs(fulldir)
        print ("\n")
        print ("Saving...")
        print ("\n")
        print (f"Membuat folder {fulldir}...")
        print ("\n")
        print (f"Berhasil menyimpan data di folder {fulldir}!")
    else:
        print ("\n")
        print ("Saving...")
        print ("\n")
        print (f"Berhasil menyimpan data di folder {fulldir}!")
    matrixtocsvril(Global.users,os.path.join(fulldir,"user.csv"),102,3)#Mengubah matrix users ke path yang ada , 102 = banyak index baris matrix, 3 = banyak kolom matrix
    matrixtocsvril(Global.candi,os.path.join(fulldir,"candi.csv"),100,5)#Mengubah matrix users ke path yang ada , 102 = banyak baris matrix, 3 = banyak kolom matrix
    matrixtocsvril(Global.bahan,os.path.join(fulldir,"bahan_bangunan.csv"),3,3)#Mengubah matrix users ke path yang ada , 102 = banyak baris matrix, 3 = banyak kolom matrix
