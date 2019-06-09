import getpass
i = 1
while True:
    haslo = getpass.getpass("Podaj haslo: ")
    if haslo == "okon":
        print(f'Zgadłes haslo przy {i} probie')
        break
    elif i == 3:
        print("Przekroczono limit prob podania hasla!")
        break
    else:
        i = i+1
        continue
