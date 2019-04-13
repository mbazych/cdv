import mysql.connector
import interfejs
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="klienci"
    )
except:
    print("Błąd! Nie można połączyć się z bazą danych MYSQL!")
    exit()

mycursor = mydb.cursor(buffered=True)

def sprawdzlogin(log, has):
        uzytkownik = []
        sqlh = "SELECT * FROM Dane WHERE login =%s AND haslo =%s"
        mycursor.execute(sqlh, (log, has))
        dane = mycursor.fetchall()
        for x in dane:
            uzytkownik.append(x)
        if dane:
            return uzytkownik
        else:
            return 0


def dodaj(login, haslo, imie, nazwisko, stan_konta, nr_tel, email):

    sqlh = "INSERT INTO Dane(login,haslo,imie,nazwisko,stan_konta,nr_tel,email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sqlh, (login, haslo, imie, nazwisko, 0, nr_tel, email))
    mydb.commit()
    return


def wplac(kwota, im, pas):
    if not all(x.isdigit() for x in kwota):
        return 1
    try:
        if int(kwota) <=0:
            return 1
    except:
        return 1
    else:
        sqlh    = "SELECT stan_konta FROM Dane WHERE login =%s AND haslo = %s"
        mycursor.execute(sqlh, (im, pas))
        ilosc   = mycursor.fetchall()
        final   = ilosc[0][0]
        kwota = int(final) + int(kwota)
        if kwota > 10000000:
            return 1
        sqlh    = "UPDATE Dane SET stan_konta=%s WHERE login = %s"
        mycursor.execute(sqlh, (kwota,im))
        mydb.commit()
        return 0


def wyplac(kwota, im, pas):
    if not all(x.isdigit() for x in kwota):
        return 1
    try:
        if int(kwota) <=0:
            return 1
    except:
        return 1
    else:
        sqlh    = "SELECT stan_konta FROM Dane WHERE login =%s AND haslo = %s"
        mycursor.execute(sqlh, (im, pas))
        ilosc   = mycursor.fetchall()
        final   = ilosc[0][0]
        kwota = int(final) - int(kwota)
        if int(kwota) < 0:
            return 1
        else:
            sqlh    = "UPDATE Dane SET stan_konta=%s WHERE login = %s"
            mycursor.execute(sqlh, (kwota,im))
            mydb.commit()
            return 0

def update(kwota, im, pas):
    sqlh    = "SELECT stan_konta FROM Dane WHERE login =%s AND haslo = %s"
    mycursor.execute(sqlh, (im, pas))
    ilosc   = mycursor.fetchall()
    final   = ilosc[0][0]
    return final


def zamknij(im,has):
    sqlh    = "DELETE FROM Dane WHERE login = %s AND haslo = %s"
    mycursor.execute(sqlh, (im,has))
    mydb.commit()


def zmien(logger, oD):
    sqlh = "UPDATE Dane SET zdjecie=%s WHERE login = %s"
    mycursor.execute(sqlh, (oD, logger))
    mydb.commit()
