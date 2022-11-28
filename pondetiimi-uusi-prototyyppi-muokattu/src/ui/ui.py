from services.konsoli_io import KonsoliIO
from services.reference_manager import ReferenceManager

class UI:
    def __init__(self, io, reference_manager):
        self._io = io
        self.reference_manager = reference_manager

    def run(self):
        while True:
            print()
            print("Komento 'uusi' luo uuden lähdeviitteen")
            print("Komento 'listaa' listaa kaikki lähdeviitteet")
            print("Komento 'vie' vie lähdeviitteet bibtex-tiedostoon")
            print("Komento 'lopeta' lopettaa ohjelman")

            komento = self._io.lue("Anna komento: ")

            if komento == "uusi":
                luetut_viitteet = self._io.lue_viitteet()
                self.reference_manager.vie_viite_databaseen(luetut_viitteet)
            elif komento == "listaa":
                viitteet = self.reference_manager.listaa_viitteet()
                self._io.tulosta(viitteet)
            elif komento == "vie":
                tiedostonimi = self._io.lue("Anna tiedostonimi:")
                self.reference_manager.vie_viitteet_tiedostoon(tiedostonimi)
            elif komento == "lopeta":
                break
