def func():
    osoba = {
        "imie": "Michał",
        "nazwisko": "Bazych",
        "samochod": "Mercedes C class",
        "miasto": "Poznań",
        "wiek": 20
        }
    osoba2 = {
        "imie": "Mateusz",
        "nazwisko": "Czarczyński",
        "samochod": "Volkswagen Passat",
        "miasto": "Czaplinek",
        "wiek": 10
    }
    print("Którą osobe wywietlić?")
    print("1 - osoba")
    print("2 - osoba2")
    wybor = input("Podaj wybor: ")
    if wybor == "1":
        for key, value in osoba.items():
            print(f'{key}: {value}')
    if wybor == "2":
        for key, value in osoba2.items():
            print(f'{key}: {value}')
    else:
        print("Zły wybór!")
        func()


if __name__ == '__main__':
    func()
