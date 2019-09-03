# sqllite_test.py

# Create a database and establishing connection to database 
import sqlite3
conn = sqlite3.connect('Mapa_aplikacji4.db')
c = conn.cursor()

# Create main table
c.execute('''CREATE TABLE Aplikacje ('Numer aplikacji', 'Nazwa aplikacji', 'Data wdrożenia', 'Wersja aktualna', 'Poprzednie wersje', 'Kopia zapasowa', 'Realizowane zadania', 'Język programowania', 'Statystyki funkcjonowania', 'Sugestie użytkowników', 'Powiązania z innymi aplikacjami') ''')


# Inserting data
c.execute('''INSERT INTO Aplikacje VALUES ('001', 'Aplikacja 1', '01.12.2012', '4.0', '3.0', '_Programy', '500+', 'C++', '20', 'Nie nadaje się', 'Aplikacja 3 jako źródło danych') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('002', 'Aplikacja 2', '15.05.2006', '3.5', '3.4', '_Programy', 'Karta wielkiej rodziny', 'Java', '80', 'Potrzebne nowe funkcjonalności', 'Aplikacja 3 jako źródło danych') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('003', 'Aplikacja 3', '17.05.2003', '2.44', '2.43', '_Programy', 'Becikowe', 'Kotlin', '50', 'Nie działa', 'Aplikacja 1 i Aplikacja 2 mogą czerpać dane') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('004', 'Aplikacja 4', '22.07.1944', '3.0', '2.0', '_Programy', 'Dowody osobiste', 'Java', '50', 'Wolno chodzi', 'Niezależna aplikacja') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('005', 'Aplikacja 5', '04.07.1977', '1.0', '1.0', '_Programy', 'Dowody rejestracyjne', 'Python 2.7', '11', 'Nie drukuje', 'Może pobierać dane z hurtowni danych') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('006', 'Aplikacja 6', '08.08.2019', '1.13', '1.12', '_Programy', 'Urodzenia', 'Python 3.7', '14', 'Jest super', 'Brak wskazań') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('007', 'Aplikacja 7', '01.04.1999', '3.8', '3.7', '_Programy', 'Zgony', 'VBA', '10', 'Skasujcie to', 'Nie działa API') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('008', 'Aplikacja 8', '01.05.1996', '4.9', '4.8', '_Programy', 'Śluby', 'HTML', '55', 'Nie działa na drukarce sieciowej', 'Nie działa API') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('009', 'Aplikacja 9', '01.01.2000', '11', '10', '_Programy', 'Zajęcie pasa drogowego', 'C++', '80', 'Złe manu główne nie ma funkcji', 'Nie ma takich funkcjonalności') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('010', 'Aplikacja 10', '01.04.2011', '22', '21', '_Programy', 'Gospodarowanie mieniem GMK', 'C', '99', 'Doskonała aplikacja', 'Wspólny serwer druku') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('011', 'Aplikacja 11', '09.07.1998', '32', '31', '_Programy', 'Zameldowania', 'Java', '44', 'Nie ma dostępu do archiwum danych', 'Wspólny serwer druku') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('012', 'Aplikacja 12', '04.05.1994', '2.8', '2.7', '_Programy', 'Wymeldowania', 'Python 3.7', '21', 'Btrak', 'Wspólny serwer druku') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('013', 'Aplikacja 13', '16.04.2008', '3.9', '3.8', '_Programy', 'Cokolwiek innego', 'Java', '22', 'Nie drukuje duplikatów', 'Wspólny serwer druku') ''')
c.execute('''INSERT INTO Aplikacje VALUES ('014', 'Aplikacja 14', '03.03.2003', '1.2', '1.1', '_Programy', 'Karty parkingowe', 'PHP', '75', 'Potrzeba dodać emaila', 'Wspólny serwer druku') ''')

# Selecting data

for row in c.execute('''SELECT * FROM Aplikacje'''):
    print(row)
conn.commit()
