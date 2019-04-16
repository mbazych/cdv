import math
import random
# pi

pi = math.pi

print(pi)

# pierwiastek

pierwiastek = math.sqrt(9)
print(pierwiastek)

# moduł random

losuj = random.random()
print(losuj)

losujZlisty = random.choice([1,2,3.33,3,4])

print(losujZlisty)

'''
    Zadanie domowe
    Użytkownik podaje z klawiatury dwie wartości, maksymalną i minimalną przedziału z którego będzie wylosowane
    5 liczb całkowitych, wylosowane liczby wyświetl w formacie:
    Liczba1
'''
min = int(input("Podaj dolny zakres"))
max = int(input("Podaj dolny zakres"))
liczby = []
wylosowane = []
for x in range(min,max):
    liczby.append(x)

for x in range(min,max):
    wylosowane.append(random.choice(liczby))
    print("Liczba %s: %s" % (x+1,wylosowane[x-1]))
