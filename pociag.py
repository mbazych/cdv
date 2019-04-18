from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout  # QMessageBox
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt


class Interfejs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):

        zdjecie = QLabel(self)
        login = QLabel("Login:", self)
        haslo = QLabel("Hasło:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(zdjecie, 0, 1)
        ukladT.addWidget(login, 1, 0)
        ukladT.addWidget(haslo, 2, 0)

        self.loginEdt = QLineEdit()
        self.hasloEdt = QLineEdit()
        self.hasloEdt.setEchoMode(QLineEdit.Password)

        ukladT.addWidget(self.loginEdt, 1, 1)
        ukladT.addWidget(self.hasloEdt, 2, 1)

        koniecBtn = QPushButton("Koniec", self)
        loginBtn = QPushButton("Zaloguj", self)
        rejestrujBtn = QPushButton("Rejestracja", self)

        koniecBtn.clicked.connect(self.koniec)
        # koniecBtn.clicked.connect(self.zaloguj)
        # koniecBtn.clicked.connect(self.mureczek)

        ukladH = QHBoxLayout()
        ukladH.addWidget(loginBtn)
        ukladH.addWidget(rejestrujBtn)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladT.addWidget(loginBtn, 3, 0, 1, 3)
        ukladT.addWidget(rejestrujBtn, 4, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 5, 0, 1, 3)

        self.setLayout(ukladT)

        self.setGeometry(500, 500, 300, 400)
        self.setFixedSize(300, 400)
        self.setWindowTitle("Login")
        self.show()

    def koniec(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    okno = Interfejs()
    sys.exit(app.exec_())
