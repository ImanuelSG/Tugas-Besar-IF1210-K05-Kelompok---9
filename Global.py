# Untuk Menyimpan Semua Data (Misal Database [0] = ['username','password','role'])
Database = ["" for i in range(103)]

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

# Buka file csv dan melakukan pengisian Database melalui fungsi split_csv
with open("user.csv","r") as file : 
    idx = 0
    for line in file :
        Database[idx] = split_csv(line)
        idx += 1
