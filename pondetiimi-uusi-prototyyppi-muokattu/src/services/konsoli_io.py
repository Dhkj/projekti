class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)

    def tulosta(self, teksti):
        print(teksti)

    def tulosta(self, viitteet):
        for viite in viitteet:
            print(viite)

    def lue_viitteet(self):
        author = self.lue("Kirjoittaja:")
        title = self.lue("Otsikko:")
        publisher = self.lue("Julkaisija:")
        year = self.lue("Vuosi:")
        isbn = self.lue("ISBN:")

        viite = {"author": author,
                 "title": title,
                 "publisher": publisher,
                 "year": year,
                 "isbn": isbn,
                 "ID": "SukunimiVuosi",
                 "ENTRYTYPE": "book"}

        return viite