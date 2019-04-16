slownik = {'klucz1':'wartosc1',  'klucz2':'wartosc2'}

'''
    Utwórz słownik o nazwie pracownik zawierający klucze:
    imie, nazwisko, miasto, wiek, imionaDzieci, imionaRodzicow
'''

pracownik = {
    'imie': 'Michał',
    'nazwisko': 'Bazych',
    'miasto': 'Trzebiatów',
    'wiek': 20,
    'imionaDzieci': ['Jan', 'Staś', 'Klaudia'],
    'imionaRodzicow': ('Maria', 'Ireneusz')
}

print(pracownik)

pracownik['wzrost'] = 175 # dodanie
pracownik['waga'] = 75 # dodanie

print(pracownik)

###############################

pracownik1 = {
    'imie': 'Anna',
    'nazwisko': 'Nowak',
    'miasto': 'Trzebiatów',
    'wiek': 20
}
print()
print(pracownik1)

klucz = 'wiek'

if klucz in pracownik1:
    del pracownik1[klucz]
    print(f'Klucz {klucz} został usunięty')
else:
    print(f'Klucz {klucz} nie został usunięty')

print(pracownik1)
print(pracownik1.keys())
print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=' ')
    print()


for key, value in pracownik1.items():
    print(f'{key}: {value}')
