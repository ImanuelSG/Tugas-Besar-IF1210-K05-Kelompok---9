def exit() :
    isVarCorrect = False # Boolean untuk mengecek apakah variabel yang dimasukkan benar atau salah
    while isVarCorrect == False :
        YorN = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if YorN == "y" or YorN == "Y" or YorN == "n" or YorN == "N" :
            print("SUdah berhasil keluar")
            isVarCorrect = True
        else : # Variabel yang dimasukkan salah
            isVarCorrect = False