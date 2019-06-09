#include <iostream>
#include <limits>

using namespace std;

double podaj(long double x) {

	bool petla = true;

	while (petla) {
		cin >> x;
		if (!cin.fail()) {
			petla = false;
		}
		else
			cout << "To nie jest liczba" << endl;
		cin.clear();
		cin.ignore(numeric_limits < streamsize >::max(), '\n');
	}

	return x;
}
double licz(double pr) {
	cout << "Obliczanie ..." << endl;
	if (pr == 0) {
		return 0;
	}
	else {
		long double licznik = 0;

		while (licznik*licznik < pr) {
			licznik++;
		}
		long double x = pr;
		long double x1 = (licznik - 1)*(licznik - 1);
		long double x2 = (licznik)*(licznik);
		long double x3 = (licznik + 1)*(licznik + 1);
		long double l0 = ((x - x2) / (x1 - x2))*((x - x3) / (x1 - x3));
		long double l1 = ((x - x1) / (x2 - x1))*((x - x3) / (x2 - x3));
		long double l2 = ((x - x2) / (x3 - x2))*((x - x1) / (x3 - x1));

		long double wynik = (licznik - 1)*l0 + licznik * l1 + (licznik + 1)*l2;

		return wynik;
	}
}

int main(int argc, char** argv) {
	setlocale(LC_ALL, "");
	cout << "Liczenie pierwiastków Lagrangea" << endl;
	bool ptl = true;
	while (ptl) {
		cout << "Podaj pierwiastek do policzenia" << endl;
		long double pr;
		do {
			pr = podaj(pr);
			if (pr < 0) {
				cout << "Pierwiastek nie może być ujemny" << endl;
			}
		} while (pr < 0);

		cout << "Wynik pierwiastkowania " << pr << " wynosi : " << licz(pr) << endl;
	}
	return 0;
}
