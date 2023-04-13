import Global

def lenn(abc):#Function untuk mendapatkan panjang dari suatu str
    length=0
    for i in abc:
        length+=1
    return length
def isValidPassword(abc):#Function untuk menentukan apakah password valid
    if (5<= lenn(abc) <=25):
        return True
    else :
        return False
def isUniqueUsername(abc,list):#Function untuk menentukan apakah username yang dimasukkan unique
    i=1
    unique = True
    while list[i]!=['','','']:
        if abc== list[i][0] :
            unique = False
            break 
        if i == 102:
            break
        i+=1  
    return unique
def getsmallestindex(list,N):#Function untuk mendapatkan indexterkecil yang masi kosong
    i=0
    while list[i]!=['','','']:
        i+=1
        if i == N:
            break
    return i
def isRegistered(user, password):
    benar = False
    for i in range(1,103):
        if Global.users[i][0] == user and Global.users[i][1] == password:
                benar = True
                break
    return benar
def SummonJin ():
    if (Global.jumlahjinpembangun + Global.jumlahjinpengumpul <= 100):
        print(f"Jenis jin yang dapat dipanggil:")
        print(f"(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print (f"(2) Pembangun - Bertugas membangun candi \n")
        pilihan = int (input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        print ("")
        while pilihan != 1 and pilihan !=2:
            print(f'Tidak ada jenis jin bernomor "{pilihan}"!')
            print ("")
            pilihan = int (input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            print ("")
        if pilihan == 1 :
            print (f'Memilih jin "Pengumpul".')
            Global.jumlahjinpengumpul+=1
        else :
            print (f'Memilih jin "Pembangun".')
            Global.jumlahjinpembangun+=1
        namajin=(input(("Masukkan username jin: ")))
        while not isUniqueUsername(namajin,Global.users):
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



