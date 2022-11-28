class ReferenceManager:
    def __init__(self, db_service):
        self.db_service = db_service  

    def vie_viite_databaseen(self, viite):
        self.db_service.vie_viite_databaseen(viite)

    def listaa_viitteet(self):
        return self.db_service.listaa_viitteet()

    def vie_viitteet_tiedostoon(self, tiedostonimi):
        self.db_service.vie_viitteet_tiedostoon(tiedostonimi)
