from colorama import Fore, Back, Style

# POPRAWIĆ ŻEBY WYŚWIETLAŁO ZAMIAST +-x TYLKO -
while True:
    print(Fore.GREEN + "            Kwadratura Simpsona")
    print(Style.RESET_ALL + "  b")
    print(" \u222Bf(x)dx")
    print("a")
    try:
        parA = float(input("Podaj a: "))
        parB = float(input("Podaj b: "))
    except:
        print("Wystąpił błąd!")
        continue


    while True:
        print("[1]Liniowa")
        print("[2]Kwadratowa")
        print("[3]Powrót")
        wybor = input("Podaj rodzaj funkcji: ")
        if wybor == '1':
            print("")
            print(Fore.RED + "f(x) = ax+b")
            print(Style.RESET_ALL)
            try:
                a = input("Podaj parametr a: ")
                b = input("Podaj parametr b: ")
                if "." not in str(a):
                    a = int(a)
                else:
                    a = float(a)
                if "." not in str(b):
                    b = int(b)
                else:
                    b = float(b)
            except:
                print("Wystąpił błąd!")
                continue

            wynik = (parB-parA)/6.0 *( (a*parA+b) + 4.0 * (a*((parA+parB)/2.0)+b) + (a*parB+b))
            if b == 0 and a == 0:
                print("Całka z 0 wynosi 0.")
                continue
            elif a == 1:
                a = None
            elif a == 0 and b < 0:
                print("Całka z {} wynosi -x.".format(b))
                continue
            elif a == 0:
                print("Całka z {} wynosi x.".format(b))
                continue
            elif b == 0:
                print("Całka z {}x wynosi {}.".format(a, wynik))
                continue
            else:
                print("Całka wynosi {}.".format(wynik))

            try:
                print("Całka z {}x+{} wynosi {}.".format(a,b,wynik))
                continue
            except:
                print("Całka z x+{} wynosi {}.".format(b, wynik))
                continue
        elif wybor == '2':
            print("")
            print(Fore.RED + "f(x) = ax^2+bx+c")
            print(Style.RESET_ALL)
            try:
                a = input("Podaj parametr a: ")
                b = input("Podaj parametr b: ")
                c = input("Podaj parametr c: ")

                if "." not in str(a):
                    a = int(a)
                else:
                    a = float(a)
                if "." not in str(b):
                    b = int(b)
                else:
                    b = float(b)
                if "." not in str(c):
                    c = int(c)
                else:
                    c = float(c)
            except:
                print("Wystąpił błąd!")
                continue

            wynik = (parB-parA)/6.0 *( (a*parA**2+b*parA+c) + 4.0 * (a*((parA+parB)/2.0)**2+b*((parA+parB)/2.0)+c) + (a*parB**2+b*parB+c))

            if b == 0 and a == 0 and c == 0:
                print("Całka z 0 wynosi 0.")
                continue
            elif a == 0 and b == 0 and c > 0:
                print("Całka z {} wynosi x.".format(c))
                continue
            elif a == 0 and b == 0 and c < 0:
                print("Całka z {} wynosi -x.".format(c))
                continue
            elif a == 0 and b != 0 and c == 0:
                print("Całka z {}x wynosi {}".format(b, wynik))
                continue
            elif a == 0 and b != 0 and c != 0:
                print("Całka z {}x+{} wynosi {}".format(b, c, wynik))
                continue
            elif a != 0 and b == 0 and c == 0:
                print("Całka z {}x^2 wynosi {}".format(a, wynik))
                continue
            elif a != 0 and b != 0 and c == 0:
                print("Całka z {}x^2+{}x wynosi {}".format(a, b, wynik))
                continue
            elif a != 0 and b == 0 and c != 0:
                print("Całka z {}x^2+{} wynosi {}".format(a, c, wynik))
                continue
            elif a != 0 and b != 0 and c != 0:
                print("Całka z {}x^2+{}x+{} wynosi {}".format(a, b, c, wynik))
                continue
            else:
                print("Całka wynosi {}".format(wynik))
                continue
        elif wybor == '3':
            break
        else:
            continue
