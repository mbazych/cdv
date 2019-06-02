while True:
    try:
        dlugosc = int(input("Ile wierszy: "))
    except ValueError:
        print("Błąd!")
    znak = input("Podaj znak: ")
    for i in range(1, dlugosc+1):
        print(i*f'{znak}')
