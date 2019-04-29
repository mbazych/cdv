def show(name):
    print(f'Przed modyfikacja: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'Po modyfikacji: {id(name)}')
data = ['Anna', 'Agnieszka', 'Andrzej']

print(f'Przed wywołaniem: {id(data)}')
show(data)

print(f'Po wywołaniu: {id(data)}')


# słownik

data1 = {
    0: 'Artur',
    1: 'Andrzej'
}

print(f'Przed wywołaniem: {id(data1)}')
show(data1)
print(f'Po wywołaniu: {id(data1)}')

# przekazywanie argumentów przed wartosci

def show1(city):
    print(f'Przed modyfikacja: {city}')
    city[0] = 'Berlin'
    city[1] = 'Bukareszt'
    print(f'Po modyfikacji: {city}')
    print(f'Po modyfikacji: {id(city)}')

miasto = {
    0: "Poznań",
    1: "Gniezno"
}

print(f'Przed wywołaniem funkcji show1: {miasto}')
print(f'Id obiektu: {id(miasto)}')
show1(dict(miasto))
print(f'Po wywołaniu funkcji show1: {miasto}')
