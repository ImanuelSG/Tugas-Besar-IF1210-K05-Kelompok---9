def getsmallestindex(list):
    i=2
    while list[i]!='':
        i+=1
    return i
Database = ["" for i in range(101)]
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
def read_csv(file) :
    with open("user.csv","r") as file : 
        idx = 0
        for line in file :
            Database[idx] = split_csv(line)
            idx += 1
def isUniqueUsername(abc,list):#Function untuk menentukan apakah username yang dimasukkan unique
    i=1
    unique = True
    while list[i]!='':
        if abc== list[i][0] :
            unique = False
            break 
        i+=1  
    return unique
read_csv("user.csv")
print (Database)
print (getsmallestindex(Database))
print (isUniqueUsername("Bondowoso",Database))
