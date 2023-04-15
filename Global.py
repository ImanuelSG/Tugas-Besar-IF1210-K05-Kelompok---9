users = [[""for j in range (3)] for i in range(103)] #Matriks users
candi = [[""for j in range (5)] for i in range (101)] #Matriks candi
bahan = [[0 for j in range (3)] for i in range (4)] #Matriks bahan-bahan

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
def read_csv(file,arr) :
    with open(file,"r") as file : 
        idx = 0
        for line in file :
            arr[idx] = split_csv(line)
            idx += 1

def read_csv_candi(file,arr):#
    with open(file,"r") as file : 
        idx = 0
        for line in file :
            if idx!= 0:
                if split_csv(line)[0]!='':
                    for j in range (5):
                        if j == 1 :
                            arr[idx][j]= split_csv(line)[j]
                        else :
                            arr[idx][j]= int(split_csv(line)[j])
                else:
                    arr[idx] = split_csv(line)
            else:
                arr[idx] = split_csv(line)
            idx += 1

def getbiggestindex(arr,N):#Fungsi untuk mendapatkan panjang array yang terisi
    for i in range (N,-1,-1):
        if arr[i][0]!='':
            hasil = i
            break
    return hasil


def isRegisteredJin(user):#Untuk mengecek apakah jin tergeistrasi dan mengembalikan indexnya jika memang ada
    benar = 999
    for i in range(3,103):
        if Global.users[i][0] == user:
                benar = i
                break
    return benar