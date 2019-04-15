from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
import baza
import main
from validate_email import validate_email

class Logowanie(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()


    def interfejs(self):
        zdjecie = QLabel(self)
        etykieta1 = QLabel("Login:", self)
        etykieta2 = QLabel("Hasło:", self)

        pixmap = QPixmap('user.png')
        pixmap = pixmap.scaled(200, 200)
        zdjecie.setPixmap(pixmap)

        ukladT = QGridLayout()
        ukladT.addWidget(zdjecie, 0, 1)
        ukladT.addWidget(etykieta1, 1, 0)
        ukladT.addWidget(etykieta2, 2, 0)

        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.Password)

        ukladT.addWidget(self.login, 1, 1)
        ukladT.addWidget(self.haslo, 2, 1)

        koniecBtn = QPushButton("&Koniec", self)
        loginBtn = QPushButton("&Zaloguj", self)
        rejestrujBtn = QPushButton("&Rejestracja", self)

        koniecBtn.clicked.connect(self.koniec)
        loginBtn.clicked.connect(self.zaloguj)
        rejestrujBtn.clicked.connect(self.mureczek)

        ukladH = QHBoxLayout()
        ukladH.addWidget(loginBtn)
        ukladH.addWidget(rejestrujBtn)

        koniecBtn.resize(koniecBtn.sizeHint())


        ukladT.addLayout(ukladH, 3, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 4, 0 ,1, 3)

        self.setLayout(ukladT)

        self.setGeometry(500, 500, 300, 400)
        self.setFixedSize(300,400)
        self.setWindowTitle("System bankowy")
        self.setWindowIcon(QIcon('user.png'))
        self.show()

    def zaloguj(self):
        loggin = self.login.text()
        hasslo = self.haslo.text()
        if baza.sprawdzlogin(loggin, hasslo)==0:
            self.blad()
        else:
            self.mureczek2()

    def koniec(self):
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Return:
            self.zaloguj()

    def blad(self):
        QMessageBox.critical(self, "Złe hasło", "Podałeś złe hasło lub login.")
        return

    def mureczek(self):
        self.child_win = Rejestracja()
        self.close()
        self.child_win.show()

    def mureczek2(self):
        im = self.login.text()
        has = self.haslo.text()
        self.child_win = Zalogowany(im, has)
        self.close()
        self.child_win.show()


class Rejestracja(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        loginLabel  = QLabel("Login: ", self)
        hasloLabel  = QLabel("Hasło: ", self)
        imie        = QLabel("Imię: ", self)
        nazwisko    = QLabel("Nazwisko: ", self)
        nr_tel      = QLabel("Nr telefonu: ", self)
        email       = QLabel("Email:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(loginLabel, 0, 0)
        ukladT.addWidget(hasloLabel, 1, 0)
        ukladT.addWidget(imie, 2, 0)
        ukladT.addWidget(nazwisko, 3, 0)
        ukladT.addWidget(nr_tel, 4, 0)
        ukladT.addWidget(email, 5, 0)

        self.loginEdit      = QLineEdit()
        self.hasloEdit      = QLineEdit()
        self.imieEdit       = QLineEdit()
        self.nazwiskoEdit   = QLineEdit()
        self.nr_telEdit     = QLineEdit()
        self.emailEdit      = QLineEdit()
        self.hasloEdit.setEchoMode(QLineEdit.Password)

        ukladT.addWidget(self.loginEdit, 0, 1)
        ukladT.addWidget(self.hasloEdit, 1, 1)
        ukladT.addWidget(self.imieEdit, 2, 1)
        ukladT.addWidget(self.nazwiskoEdit, 3, 1)
        ukladT.addWidget(self.nr_telEdit, 4, 1)
        ukladT.addWidget(self.emailEdit, 5, 1)

        wrocBtn     = QPushButton("&Wróć", self)
        stworzBtn   = QPushButton("&Stwórz konto", self)

        wrocBtn.resize(wrocBtn.sizeHint())
        stworzBtn.resize(stworzBtn.sizeHint())

        stworzBtn.clicked.connect(self.sprawdz)
        wrocBtn.clicked.connect(self.powrot)

        ukladT.addWidget(wrocBtn, 6, 0, 1, 3)
        ukladT.addWidget(stworzBtn, 7, 0, 1, 3)

        self.setLayout(ukladT)
        self.setWindowIcon(QIcon('user.png'))
        self.setGeometry(500, 500, 300, 400)
        self.setFixedSize(300,400)
        self.setWindowTitle("Rejestracja")
        self.show()

    def koniec(self):
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Return:
            self.zaloguj()


    def sprawdz(self):
        is_valid = validate_email(self.emailEdit.text())

        # login

        if len(self.loginEdit.text()) < 3 or len(self.loginEdit.text()) > 12:
            QMessageBox.warning(self, "Błąd", "Podany login jest za długi lub za krótki!")

        # hasło

        elif len(self.hasloEdit.text()) < 8 or len(self.hasloEdit.text()) > 20:
            QMessageBox.warning(self, "Błąd", "Podane hasło jest za długie lub za krótkie!")
        elif not any(x.isupper() for x in self.hasloEdit.text()):
            QMessageBox.warning(self, "Błąd", "Hasło musi zawierać jedną wielką literę, jedną małą oraz cyfrę!")
        elif not any(x.islower() for x in self.hasloEdit.text()):
            QMessageBox.warning(self, "Błąd", "Hasło musi zawierać jedną wielką literę, jedną małą oraz cyfrę!")
        elif not any(x.isdigit() for x in self.hasloEdit.text()):
            QMessageBox.warning(self, "Błąd", "Hasło musi zawierać jedną wielką literę, jedną małą oraz cyfrę!")

        # imie

        elif any(x.isdigit() for x in self.imieEdit.text()):
            QMessageBox.warning(self, "Błąd", "Podaj prawidłowe imię!")
        elif len(self.imieEdit.text()) < 3:
            QMessageBox.warning(self, "Błąd", "Podaj prawidłowe imię!")

        # nazwisko

        elif any(x.isdigit() for x in self.imieEdit.text()):
            QMessageBox.warning(self, "Błąd", "Podaj prawidłowe nazwisko!")
        elif len(self.nazwiskoEdit.text()) < 3:
            QMessageBox.warning(self, "Błąd", "Podaj prawidłowe nazwisko!")
        # nr telefonu

        elif not all(x.isdigit() for x in self.nr_telEdit.text()):
            QMessageBox.warning(self, "Błąd", "Podaj prawidłowy numer telefonu!")
        elif not len(self.nr_telEdit.text()) == 9:
            QMessageBox.warning(self, "Błąd", "Podaj prawidłowy numer telefonu!")

        # email

        elif not is_valid:
            QMessageBox.warning(self, "Błąd", "Podany email jest nieprawidłowy!")
        else:
            self.imieEdit.text().capitalize()
            self.nazwiskoEdit.text().capitalize()
            baza.dodaj(self.loginEdit.text(), self.hasloEdit.text(), self.imieEdit.text(), self.nazwiskoEdit.text(), 0, self.nr_telEdit.text(), self.emailEdit.text())
            QMessageBox.information(self, "Konto utworzone", "Utworzyłeś konto! Możesz się teraz zalogować")
            self.powrot()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.powrot()
        elif e.key() == Qt.Key_Return:
            self.sprawdz()


    def powrot(self):
        self.child_win = Logowanie()
        self.close()
        self.child_win.show()


class Zalogowany(QWidget):

    def __init__(self, im, has):
        super().__init__()
        self.im     = im
        self.has    = has
        self.interfejs(im, has)

    def interfejs(self, im, has):
        self.prof                = QLabel(self)
        uzytkownik          = []
        uzytkownik          = baza.sprawdzlogin(im,has)
        self.stan_konta     = QLabel("Stan konta: {}PLN".format(uzytkownik[0][5]), self)
        self.imienazwisko   = QLabel("{} {}".format(uzytkownik[0][3],uzytkownik[0][4]), self)
        kwota               = QLabel("Kwota:", self)
        logger              = uzytkownik[0][1]
        passer              = uzytkownik[0][2]
        self.pixmap         = QPixmap("{}".format(uzytkownik[0][8]))
        self.pixmap         = self.pixmap.scaled(150,150)
        self.prof.setPixmap(self.pixmap)

        ukladT = QGridLayout()
        ukladT.addWidget(self.prof, 0, 0)
        ukladT.addWidget(self.stan_konta, 1, 2)
        ukladT.addWidget(self.imienazwisko, 0, 2)
        ukladT.addWidget(kwota, 2, 0)

        self.ile = QLineEdit()
        ukladT.addWidget(self.ile, 2, 2)

        wplacBtn    = QPushButton("&Wpłać", self)
        wyplacBtn   = QPushButton("&Wypłać", self)
        infoBtn     = QPushButton("&Pokaż informacje", self)
        wylogujBtn  = QPushButton("&Wyloguj", self)
        zamknijBtn  = QPushButton("&Zamknij konto", self)
        zmienBtn    = QPushButton("Zmień zdjęcie")

        wplacBtn.clicked.connect(lambda: self.wplac(logger, passer))
        wyplacBtn.clicked.connect(lambda: self.wyplac(logger, passer))
        infoBtn.clicked.connect(lambda: self.info(uzytkownik))
        wylogujBtn.clicked.connect(self.wyloguj)
        zamknijBtn.clicked.connect(lambda: self.zamknij(logger,passer))
        zmienBtn.clicked.connect(lambda: self.zmien(logger))

        wplacBtn.resize(wplacBtn.sizeHint())
        wyplacBtn.resize(wyplacBtn.sizeHint())
        infoBtn.resize(infoBtn.sizeHint())
        wylogujBtn.resize(wylogujBtn.sizeHint())
        zamknijBtn.resize(zamknijBtn.sizeHint())

        ukladT.addWidget(zmienBtn, 1, 0, 1, 1)
        ukladT.addWidget(wplacBtn, 3, 0, 1, 3)
        ukladT.addWidget(wyplacBtn, 4, 0, 1, 3)
        ukladT.addWidget(infoBtn, 5, 0, 1, 3)
        ukladT.addWidget(wylogujBtn, 6, 0, 1, 3)
        ukladT.addWidget(zamknijBtn, 7, 0, 1, 3)

        self.setLayout(ukladT)
        self.setWindowIcon(QIcon('user.png'))
        self.setGeometry(500, 500, 200, 200)
        self.setFixedSize(320, 400)
        self.setWindowTitle("System Bankowy")
        self.show()


    def wplac(self, logger, passer):
        kwota = self.ile.text()
        if baza.wplac(kwota, logger, passer) == 1:
            QMessageBox.critical(self, "Błąd", "Podaj prawidłową wartość!")
        else:
            QMessageBox.information(self, "Sukces", "Wpłaciłeś {}PLN".format(kwota))
            self.stan_konta.setText("Stan konta: {}PLN".format(baza.update(0, logger, passer)))


    def wyplac(self, logger, passer):
        kwota = self.ile.text()
        if baza.wyplac(kwota, logger, passer) == 1:
            QMessageBox.critical(self, "Błąd", "Podaj prawidłową wartość!")
        else:
            QMessageBox.information(self, "Sukces", "Wypłaciłeś {}PLN".format(kwota))
            self.stan_konta.setText("Stan konta: {}PLN".format(baza.update(0, logger, passer)))


    def info(self, uzytkownik):
            QMessageBox.information(self, "Informacje", "Login: %s<br>Imię: %s<br>Nazwisko: %s<br>Stan konta: %s<br>Numer telefonu: %s<br>E-mail: %s" % (uzytkownik[0][1],uzytkownik[0][3],uzytkownik[0][4],uzytkownik[0][5],uzytkownik[0][6],uzytkownik[0][7]))


    def zamknij(self, logger, passer):
        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno chcesz usunąć konto?<br> Stracisz pieniądze na koncie!",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            baza.zamknij(logger,passer)
            QMessageBox.information(self, "Sukces", "Twoje konto zostało usunięte!")
            self.wyloguj()
        else:
            return


    def zmien(self, logger):
        openDirectoryDialog = QFileDialog()
        oD = openDirectoryDialog.getOpenFileName(self, "open", "/home/github/bank")
        self.pixmap         = QPixmap("{}".format(oD[0]))
        self.pixmap = self.pixmap.scaled(150, 150)
        self.prof.setPixmap(self.pixmap)
        baza.zmien(logger, str(oD[0]))


    def wyloguj(self):
        self.child_win = Logowanie()
        self.close()
        self.child_win.show()
