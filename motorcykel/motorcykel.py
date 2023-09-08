
class Motorcykel:

    def __init__(self, id=None, fabrikat=None, modell=None, kubik=None, vikt=None, hk=None, topphastighet=None):
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
