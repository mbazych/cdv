
def witaj():
    print("Witaj!")


witaj()

def wyswietlWiek(wiek):
    print(f'Twój wiek to: {wiek}')


wyswietlWiek(6)

def iloczyn(a, b):
    return a*b

wynik = float(iloczyn(3, 6))

def funkcja(marka, model, pojemnosc, predkoscMax):
    samochod = {
        'Marka': marka,
        'Model': model,
        'Pojemnosc': pojemnosc,
        'Predkosc maksymalna': predkoscMax
    }
    wyswietl(samochod)

def wyswietl(samochod):
    for key,value in samochod.items():
        print(f'{key}: {value}')

funkcja(
    input("Podaj marke: "),
    input("Podaj model: "),
    input("Podaj pojemnosc: "),
    input("Podaj predkosc maksymalna: ")
)
