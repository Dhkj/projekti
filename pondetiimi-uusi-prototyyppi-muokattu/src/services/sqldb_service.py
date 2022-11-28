import sqlite3
from services.bibtex_service import BibtexService # Riippuvuus huono?

class SqldbService:
    def __init__(self):
        self.bibtex_service = BibtexService() # Riippuvuus huono?

    def vie_viite_databaseen(self, viite):
        # Tarkistus, onko viite jo db:ssä puuttuu.
        db = sqlite3.connect("test.db")
        db.isolation_level = None
        values=(viite["author"], viite["title"], viite["publisher"], viite["year"], viite["isbn"])
        db.execute("INSERT INTO test (author, title, publisher, year, isbn) VALUES (?, ?, ?, ?, ?)",values)
        db.commit()
        db.close()

        # Tarpeellinen?
        title = viite["title"]
        author = viite["author"]
        return f"Book {title} by {author} saved."

    def listaa_viitteet(self):
        viitteet = []

        db = sqlite3.connect("test.db")
        db.isolation_level = None
        all = db.execute("SELECT * FROM test")

        for row in all:
            viite = {"author": row[1],
                 "title": row[2],
                 "publisher": row[3],
                 "year": row[4],
                 "isbn": row[5],
                 "ID": "SukunimiVuosi",
                 "ENTRYTYPE": "book"}

            viitteet.append(viite)

        db.close()

        return viitteet

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        viitteet = self.listaa_viitteet()

        for viite in viitteet:
            self.bibtex_service.vie_viite_databaseen(viite) # Huono käyttää bibdatabase?

        self.bibtex_service.vie_viitteet_tiedostoon(tiedostonimi)
