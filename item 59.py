import sqlite3

connection = sqlite3.connect(':memory:')

c = connection.cursor()

c.execute("DROP TABLE IF EXISTS Roster")
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
c.execute("INSERT INTO Roster values('Jean-Baptiste Zorg', 'Human', 122)")
c.execute("INSERT INTO Roster values('Korben Dallas', 'Meat Popsicle', 100)")
c.execute("INSERT INTO Roster VALUES('Ak''not', 'Mangalore', -5)")

c.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas'")


c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
for row in c.fetchall():
    print(row)
