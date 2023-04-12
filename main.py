import Login
import Help

keluar = False
while not keluar:
    command = input(">>> ")
    if command == "login":
        Login.login()
    elif command == "help":
        Help.help()
        keluar = True

