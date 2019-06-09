import getpass

prawHaslo = "okonek"

dane = {
    "imie": "",
    "nazwisko": "",
    "wiek": ""
}

def sprawdzHaslo(haslo):
    if haslo == prawHaslo:
        print("Podałes prawidłowe hasło!")
        print("Teraz przejdziemy do czegos ciekawszego!")
        wprowadzDane(**dane)
    else:
        print("Niestety.. złe hasło!")
        wpiszHaslo()

def wprowadzDane(**kwargs):
    for key, value in kwargs.items():
        kwargs[key] = input(f"Podaj {key}: ")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
def wpiszHaslo():
    try:
        podaneHaslo = getpass.getpass("Podaj hasło: ")
        sprawdzHaslo(podaneHaslo)
    except:
        print("Cos poszlo nie tak, sprobuj jeszcze raz!")
        wpiszhaslo()


wpiszHaslo()
