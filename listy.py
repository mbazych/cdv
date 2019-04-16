programowanie = ['Python', 'PHP', 'C#', 'C++', 'JavaScript', 'Java']

print(programowanie)

pierwszy = programowanie[-6]
print(pierwszy)



try:
    x = int(input("Który od konca wyraz listy chcesz zobaczyć?  "))
    print(programowanie[-x])
except:
    print("Nie ma aż tyle wyrazów! Podaj mniejszą liczbę!")


# ZLICZANIE ELEMNTÓW W LIŚCIE

ile = programowanie.count('Python')
print(ile)

# ilosc elementow w liscie

iloscElementow = len(programowanie)
print(iloscElementow)

inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)

# czyszczenie list
nowa = programowanie
print('Lista nowa: ' ,end="")
print(nowa)

nowa.clear()
print('Lista nowa: ')
print(programowanie) # czyszczac liste polaczona
