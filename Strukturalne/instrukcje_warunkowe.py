x = 6

if x == 5:
    print("x jest równe 5!")
else:
    print("x nie jest równe 5!")


###############

y = True


if y:
    print("Prawda!")
else:
    print("Fałsz!")

z = 5 > 6

####################

if z:
    print("Prawda!")
else:
    print("Fałsz!")


# j = '1' # prawda
# j = '0' # prawda
# j = '' # fałsz
j = False
if bool(j):
    print(1)
else:
    print(0)



k = input("Podaj k: ")

if bool(k):
    print("Zmienna k zawiera dane")
else:
    print("Zmienna k nie zawiera danych")
