import datetime
import typing
time = datetime.datetime.now()

y = time.year
mn = time.month
d = time.day
h = time.hour
m = time.minute
s = time.second
seed =(y*365 + mn*30 + d)*24*60 + h*24 + m*60 + s

users = [["" for j in range (3)] for i in range(103)] #Matriks users
candi = [["" for j in range (5)] for i in range (101)] #Matriks candi
bahan = [[0 for j in range (3)] for i in range (4)] #Matriks bahan-bahan

# Fungsi untuk membagi data file csv yang dipisahkan oleh semicolon ke dalam masing-masing "kolom" array
def split_csv(line : str) -> list:
    semicolon = 1
    for i in range (len(line)) :
        if line[i] == ";" :
            semicolon += 1
    Temp = [ "" for i in range (semicolon)] # list untuk menyimpan semua data dalam 1 baris (Misal username + password + role)
    idx = 0 # Indeks untuk list Temp
    for i in range (len(line)) :
        if  line[i] == "\n" :
            idx+=1
        elif line[i] != ";":
            Temp[idx] += line[i]
        else :
            idx += 1
    return Temp

# Buka file csv, melakukan pengisian mtx (matrix) melalui fungsi split_csv, lalu mengembalikan matriks
def read_csv(file , arr)  :
    with open(file,"r") as file : 
        idx = 0
        for line in file :
            arr[idx] = split_csv(line)
            idx += 1

def read_csv_candi(file, arr) :
    with open(file,"r") as file : 
        idx = 0
        for line in file :
            if idx!= 0:
                if split_csv(line)[0]!='':
                    for j in range (5):
                        if j == 1 :
                            arr[int(split_csv(line)[0])][j]= split_csv(line)[j]
                        else :
                            arr[int(split_csv(line)[0])][j]= int(split_csv(line)[j])
                else:
                    arr[idx] = split_csv(line)
            else:
                arr[idx] = split_csv(line)
            idx += 1

def read_csv_bahan (file,arr) :
    with open(file,"r") as file : 
        idx = 0
        for line in file :
            if idx!= 0 :
                for j in range (3):
                    if j == 2:
                        arr[idx][j]= int(split_csv(line)[j])
                    else :
                        arr[idx][j]= split_csv(line)[j]
            else:
                arr[idx] = split_csv(line)
            idx += 1

def getbiggestindex(arr: list,N:int) -> int:#Fungsi untuk mendapatkan index  list yang terisi
    for i in range (N,-1,-1):
        if arr[i][0]!='':
            hasil = i
            break
    return hasil

def getsmallestindex(list: list, N: int) -> int:#Function untuk mendapatkan indexterkecil yang masi kosong
    i=0
    while list[i][0]!='':
        i+=1
        if i == N:
            break
    return i

def isRegisteredJin(user:str) -> int:#Untuk mengecek apakah jin tergeistrasi dan mengembalikan indexnya jika memang ada
    benar = 999
    for i in range(3,103):
        if users[i][0] == user:
                benar = i
                break
    return benar