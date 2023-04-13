# Untuk Menyimpan Semua Data (Misal Database [0] = ['username','password','role'])
users = ["" for i in range(103)]
candi = ["" for i in range(103)]
bahan = ["" for i in range(103)]

# Fungsi untuk membagi file csv menjadi username, password, role
def split_csv(line) :
    semicolon = 1
    for i in range (len(line)) :
        if line[i] == ";" :
            semicolon += 1
    Temp = [ "" for i in range (semicolon)] # Array untuk menyimpan semua data dalam 1 baris (Misal username + password + role)
    idx = 0 # Indeks untuk array Temp
    for i in range (len(line)) :
        if  line[i] == "\n" :
            idx+=1
        elif line[i] != ";":
            Temp[idx] += line[i]
        else :
            idx += 1
    return Temp

# Buka file csv, melakukan pengisian mtx (matrix) melalui fungsi split_csv, lalu mengembalikan matriks
def read_csv(file,mtx) :
    with open(file,"r") as file : 
        idx = 0
        for line in file :
            mtx[idx] = split_csv(line)
            idx += 1
    return mtx

users = read_csv("user.csv",users)
candi = read_csv("candi.csv",candi)
bahan = read_csv("bahan_bangunan.csv",bahan)

