import argparse
import os

def load ():
    parser = argparse.ArgumentParser()
    parser.add_argument()

def save ():
    global fulldir
    mainfolder_name = "save"
    subfolder_name = str (input("Masukkan nama folder: "))
    fulldir = os.path.join(mainfolder_name, subfolder_name)
    if not os.path.exists(mainfolder_name):
        os.makedirs(fulldir)
    elif not os.path.exists(fulldir):
        os.makedirs(fulldir)
    else:
        print ("Sudah ada")

print (fulldir)