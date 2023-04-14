import Global
from HancurkanCandi import banyak_candi

def ayamberkokok() :
    print("Kukuruyuk.. Kukuruyuk..\n")
    count = banyak_candi(Global.candi)
    print(f"Jumlah candi: {count}\n")

    if count < 100 :
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise*\n")
        print("Roro Jonggrang dikutuk jadi candi")
        quit()
    else : # count >= 100
        print("Yah, Bandung Bondowoso memenangkan permainan")
        quit()