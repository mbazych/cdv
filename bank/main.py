import interfejs
import baza


if __name__ == '__main__':
    import sys

    app = interfejs.QApplication(sys.argv)
    okno = interfejs.Logowanie()
    sys.exit(app.exec_())
