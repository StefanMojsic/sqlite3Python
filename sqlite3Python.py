import sqlite3
import sys


def stampajBazu():
    try:
        podaci = kursor.execute("SELECT ID, Fname, Lname, Age, Address, Salary, HireDate FROM Employees")

        for i in podaci:
            print("ID: ", i[0])
            print("Ime: ", i[1])
            print("Prezime: ", i[2])
            print("Godine: ", i[3])
            print("Adresa: ", i[4])
            print("Plata: ", i[5])
            print("Datum pocetka: ", i[6])
            
    except sqlite3.OperationalError:
        print("Baza ne postoji")

    except:
        print("Greska sa bazom podataka")

konekcija = sqlite3.connect('Baza.db')

print('Baza je kreirana')

kursor = konekcija.cursor()

konekcija.execute("DROP TABLE IF EXISTS Employees")
konekcija.commit()

try:
    konekcija.execute("""CREATE TABLE Employees(ID INTEGER PRIMARY KEY
                  AUTOINCREMENT NOT NULL,FName TEXT NOT NULL,
                  LName TEXT NOT NULL, Age INTEGER NOT NULL,
                  Address TEXT, Salary REAL, HireDate TEXT);""")

    konekcija.commit()

except sqlite3.OperationalError:
    print("Tabela ne moze biti napravljenja.")

konekcija.execute("""INSERT INTO Employees(FName, Lname, Age, Address,
Salary, HireDate) VALUES ('Stefan', 'Mojsic', 22, 'Mladenovac', 12333, date('now')) """)

konekcija.commit()

stampajBazu()


konekcija.close()
