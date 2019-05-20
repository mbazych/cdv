# precyzja liczby (zaokraglenie do 3 miejsc po przecinku)

x = "{0:.3f}".format(5)
print(x)
def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(iloscChf)

def plnToEuro(value):
    kursEuro = 4.29272937
    iloscEuro = value / kursEuro
    iloscEuro = int(iloscEuro)
    print(iloscEuro)

plnToChf(float(input("Podaj ilosc zlotowek na franki: ")))
plnToEuro(int(input("Podaj ilosc zlotowek na euro: ")))
# utworz funkcje zwracaja ilosc euro


def pracownik(**kwargs):
    for key, value in kwargs.items():
        print(f'Klucz {key}, wartosc {value}')

pracowniczek = {
    "imie": "Jan",
    "Nazwisko": "Kowalski",
    "wiek": 30,
    "umowa o prace": True
}

pracownik(**pracowniczek)

string = 'CDV - uczelnia ludzi ciekawych'

for char in string:
    print(char, end=" ")

print()

for i in range(1,11):
    print(i, end=" ")

#wypisz elementy z listy do momentu wartosci 'end', q lub quit

lista = ['dziura', 'mala', 'agafg', 'asdg', 'asd', 'adsg', 'quit', 'afgjafjg', 'afhghh']

for i in lista:
    if i == 'q' or i == 'quit' or i == 'exit' or i == 'end':
        break
    else:
        print(i)
