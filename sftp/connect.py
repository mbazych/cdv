import pysftp
import os
import getpass
import editor
import sys


clear = lambda: os.system('cls')


myHostname = "mars.edu.cdv.pl" # input("Serwer: ")
myPort     = 1022 # int(input("Port: "))
myUsername = "mbazych" # input("user: ")
myPassword = "XB7tEp2+" # getpass.getpass("password: ")

komendy = {  # komenda:opis
            "ls": "Wyswietla pliki w folderze w ktorym sie znajdujemy",
            "ls all": "Wyswietla pliki w folderze w ktorym sie znajdujemy oraz dodatkowe informacje",
            "upload": "Menedzer dodawania plikow na serwer",
            "download": "Menedzer sciagania plikow z serwera",
            "exit": "Wyjscie",
            "help": "Lista Komend",
            "pwd": "Wyswietla gdzie sie znajdujesz"
            }

def conn():
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, port=myPort) as sftp:
        clear()
        print("Polaczenie udalo sie!")

        # Switch to a remote directory5
        sftp.cwd('/home/uczelnia.local/mbazych')

        # Obtain structure of the remote directory '/var/www/vhosts'
        directory_structure = sftp.listdir_attr()

        while True:
            cmd = input(f'[{sftp.pwd}] ')
            cmd = cmd.capitalize()
            print(cmd[0:2])
            if cmd == 'Ls':
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    print("   " + attr.filename)
            elif cmd == 'Ls all':
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    print(attr.filename, attr)
            elif cmd == 'Upload':
                try:
                    naDysku = input("Podaj sciezke do pliku na swoim dysku: ")
                    print("Podaj sciezke gdzie ma byc zapisany plik na serwerze")
                    naSerwerze = input("Uzyj kropki aby odwolac sie do biezacego folderu:")

                    sftp.put(naDysku, naSerwerze)
                    continue
                except:
                    print("Podaj prawidlowa sciezke!")
                    continue
            elif cmd == 'Download':
                try:
                    naDysku = input("Podaj sciezke gdzie ma byc zapisany plik na twoim dysku: ")
                    print("Podaj sciezke do pliku na serwerze: ")
                    naSerwerze = input("Uzyj kropki aby odwolac sie do biezacego folderu:")

                    sftp.get(naDysku, naSerwerze)
                    continue
                except:
                    print("Podaj prawidlowa sciezke!")
                    continue
            elif cmd == 'Exit':
                exit()
            elif cmd == 'Help':
                for key, value in komendy.items():
                    print(f'{key}: {value}')
            elif cmd == 'Pwd':
                print(sftp.pwd)
            elif cmd[0:2] == 'Cd':
                if sftp.exists(cmd[3:]):
                    sftp.cwd(cmd[3:])
                else:
                    print(f'{sftp.pwd}/{cmd[3:]} nie istnieje!')
            elif cmd[0:4] == 'Edit':
                if sftp.exists(cmd[5:]):
                    naDysku = cmd[5:]
                    sftp.get(naDysku, cmd[5:])

            else:
                print("Bledna komenda!")
                continue

    # connection closed automatically at the end of the with-block
conn()
