
class Motorcykel:

    def __init__(self, id, fabrikat, modell, kubik, vikt, hk, topphastighet):
        self.id = id
        self.fabrikat = fabrikat
        self.modell = modell
        self.kubik = kubik
        self.vikt = vikt
        self.hk = hk
        self.topphastighet = topphastighet

    def getFabrikat(self):
        return self.fabrikat 
    
    def setFabrikat(self, fabrikat):
        self.fabrikat = fabrikat
