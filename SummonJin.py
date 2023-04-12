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
    while list[i]!='':
        if abc== list[i][0] :
            unique = False
            break 
        i+=1  
    return unique
def getsmallestindex(list):
    i=2
    while list[i]!='':
        i+=1
    return i
def SummonJin ():
    if (Global.Num_JinPengumpul + Global.Num_JinPembangun <= 100):
        print(f"Jenis jin yang dapat dipanggil :")
        print(f"(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print (f"(2) Pembangun - Bertugas membangun candi \n")
        pilihan = int (input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if pilihan != 1 and pilihan !=2:
            print(f"Tidak ada jenis jin bernomor ","{pilihan}!")
        elif pilihan == 1 :
            print (f"Memilih jin","Pengumpul",".")
            namajin=str(input(("Masukkan username jin: ")))
            while not isUniqueUsername(namajin,Global.user):
                print (f'Username "{namajin}" sudah diambil! \n')
                namajin=str(input(("Masukkan username jin: ")))
            Global.user[getsmallestindex(Global.Database)][0]=
        elif pilihan == 2:
            print (f'Memilih jin "Pengumpul".')
    else :
        print (f"Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")



