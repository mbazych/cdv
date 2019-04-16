# listy
imiona = ['Julia', 'Anna', 'Krystyna']
print(type(imiona))
imiona.append('Janusz')
ilosc = len(imiona)
print(f'Ilość imion:  {ilosc}')

# tuple
nazwiska = ('Kowalski', 'Nowak')
print(type(nazwiska))
print(nazwiska)
# tuple szybsze, ale nic sie nie dodaje
ilosc = len(nazwiska)
print(f'Ilość nazwisk: {ilosc}')


# słowniki

osoba = {
    'imie':'Julia',
    'nazwisko':'Nowak',
    'wiek':23
}
print(osoba, type(osoba))
print(osoba['nazwisko'])
print(osoba.keys())
print(osoba.get('wzrost', 'Brak danych'))
print(osoba.get('imie', 'Brak danych'))
