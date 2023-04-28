import Global
from Global import getbiggestindex
def isValidPassword(password:str)->bool :#Function untuk menentukan apakah password valid
    if (5<= len(password) <=25):
        return True
    else :
        return False

def isUniqueUsername(abc:str)->bool:#Function untuk menentukan apakah username yang dimasukkan unique
    i=1
    unique = True
    for i in range (1,getbiggestindex(Global.users,102)+1):
        if abc== Global.users[i][0] :
            unique = False
            break 
        if i == 102:
            break 
    return unique

def getsmallestindex(list:list,N:int)->int:#Function untuk mendapatkan indexterkecil yang masi kosong
    i=0
    while list[i][0]!='':
        i+=1
        if i == N:
            break
    return i

def getNumJinPengumpul(list:list)->int:
    count = 0
    for i in range (3,103):
        if list[i][2] == "jin_pengumpul":
            count +=1
    return count

def getNumJinPembangun(list:list)->int:
    count = 0
    for i in range (3,103):
        if list[i][2] == "jin_pembangun":
            count +=1
    return count

def SummonJin ():
    if (getNumJinPembangun(Global.users) +getNumJinPengumpul(Global.users)< 100):
        print(f"Jenis jin yang dapat dipanggil:")
        print(f"(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print (f"(2) Pembangun - Bertugas membangun candi \n")
        pilihan = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        print ("")
        while pilihan != 1 and pilihan !=2:
            print(f'Tidak ada jenis jin bernomor "{pilihan}"!')
            print ("")
            pilihan = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            print ("")
        if pilihan == 1 :
            print (f'Memilih jin "Pengumpul".')
        else :
            print (f'Memilih jin "Pembangun".')
        namajin=(input(("Masukkan username jin: ")))
        while not isUniqueUsername(namajin):
            print (f'Username "{namajin}" sudah diambil! \n')
            namajin=str(input(("Masukkan username jin: ")))
        password=(input("Masukkan password jin: "))
        while not isValidPassword(password):
            print ("Password panjangnya harus 5-25 karakter!")
            password=(input("Masukkan password jin: "))
        print ("")
        print ("Mengumpulkan sesajen...")
        print ("Menyerahkan sesajen...")
        print ("Membacakan mantra...")
        print ("")
        print (f"Jin {namajin} berhasil dipanggil!")
        n = getsmallestindex(Global.users,102)
        Global.users[n][0]=namajin
        Global.users[n][1]=password
        if pilihan == 1:
            Global.users[n][2]="jin_pengumpul"
        else :
            Global.users[n][2]="jin_pembangun"
    else :
        print (f"Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
