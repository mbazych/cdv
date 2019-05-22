try:
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    if a + b == 0:
        print("Nie dzieli się przez 0")
    else:
        c = (a*a+b)/(a+b)**2
        print(f'Wynik: {c}')
except ValueError:
    print("Błędne dane!")
