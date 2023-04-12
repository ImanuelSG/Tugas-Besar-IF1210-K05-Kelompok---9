import Global
import sys

def ayamberkokok() :
    print("Kukuruyuk.. Kukuruyuk..\n")
    count = 0 # Untuk menghitung banyak candi yang ada
    inIndex = True # Untuk flag bahwa looping dibawah masih dalam range
    i = 0
    while inIndex == True :
        if Global.Datacandi[i] != "" :
            count += 1
            i += 1
        else : # Datacandi kosong
            inIndex = False
    print(f"Jumlah candi: {count}\n")

    if count < 100 :
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*\n")
        print("Roro Jonggrang dikutuk jadi candi")
        sys.exit()
    else : # count >= 100
        print("Yah, Bandung Bondowoso memenangkan permainan")
        sys.exit()