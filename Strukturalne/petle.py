#pętle zadania
# Podaj wartość początkową i końcową, która będzie wypisana w porządku malejącym
try:
    x = int(input("Podaj wartosc poczatkowa: "))
    y = int(input("Podaj wartosc poczatkowa: "))
    if x < y:
        for i in range(y,x-1, -1):
            print(i, end=" ")
    elif x > y:
        for i in range(x, y-1, -1):
            print(i, end=" ")
    else:
        print("Wartosci sa takie same!")
except ValueError:
    print("Podaj prawidlowa wartosc!")
