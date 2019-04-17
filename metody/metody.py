import sys
from os import system, name
import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
np.seterr(divide='ignore', invalid='ignore')


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')


while True:
    print("Wartośći większe niż %s są wyświetlane w notacji naukowej lub jako + inf." % sys.maxsize)
    print("\nInterpolacja\n")
    ilosc = input("\nPodaj ilość węzłów: ")
    try:
        if int(ilosc) <= 0:
            print("\nPodałeś złą ilość węzłów!")
            continue
    except ValueError:
        print("\nPodałeś złą ilość węzłów!")
        continue
    if int(ilosc) > 0:

        wezly = []
        for x in range(1, int(ilosc)+1):
            while True:
                try:
                    tmp = input("\nPodaj x%s: " % x)
                    if float(tmp) in wezly:
                        print("\nTę wartość już podałeś!")
                        continue
                    wezly.append(float(tmp))
                    break
                except ValueError:
                    print("\nPodaj prawidłowa wartość...\n")
                    continue
        wartoscwezlow = []

        for x in range(1, int(ilosc)+1):
            while True:
                try:
                    tmp = input("\nPodaj f(x%s): " % x)
                    wartoscwezlow.append(float(tmp))
                    break
                except ValueError:
                    print("\nPodaj prawidłowa wartość...\n")
                    continue
        print("  x  = %s" % wezly)
        print("f(x) = %s" % wartoscwezlow)

        x = np.array(wezly)
        y = np.array(wartoscwezlow)
        poly = scipy.interpolate.lagrange(x, y)
        print(type(poly))
        print("\nL%s(x)=\n\n%s" % (int(ilosc)-1, poly))
        while True:
            print("\n\n     Co teraz?")
            print("     [1]Rysuj")
            print("     [2]Licz jeszcze raz!")
            print("     [3]Wyjdź")
            try:
                wybor = input("    Twój wybor: ")
            except ValueError:
                print("\n           Podałeś zły wybór!\n")
                continue
            if wybor == '1':
                plt.figure()
                u = plt.plot(x, y, 'ro')  # plot the points
                t = np.linspace(0, 1, len(x))  # parameter t to parametrize x
                # and y
                pxLagrange = scipy.interpolate.lagrange(t, x)  # X(T)
                pyLagrange = scipy.interpolate.lagrange(t, y)  # Y(T)
                n = 100
                ts = np.linspace(t[0], t[-1], n)
                xLagrange = pxLagrange(ts)  # lagrange x coordinates
                yLagrange = pyLagrange(ts)  # lagrange y coordinates
                plt.plot(xLagrange, yLagrange, 'b-', label="Interpolacja")
                plt.show()

                break
            elif wybor == '2':
                break
            elif wybor == '3':
                sys.exit()
            else:
                print("\n           Podałeś zły wybór!\n")
