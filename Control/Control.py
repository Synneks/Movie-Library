'''
Fiecare functie preia functia din Repo.py si o returneaza in Console.py
'''

class Controller_Film:
    filmRepo = None

    def __init__(self, Film_Repo):
        self.filmRepo = Film_Repo

    def read_file(self):
        return self.filmRepo.read_file()

    def write_file(self):
        return self.filmRepo.write_file()

    def afisare_film(self):
        return self.filmRepo.afisare_film()

    def add_film(self, F):
        self.filmRepo.add_film(F)

    def update_pret(self, ID, pret_nou):
        return self.filmRepo.update_pret(ID, pret_nou)

    def cautare_scor(self,scor_minim):
        return self.filmRepo.cautare_scor(scor_minim)

    def cautare_actor(self,nume_actor):
        return self.filmRepo.cautare_actor(nume_actor)

    def cautare_film(self,ID):
         return self.filmRepo.cautare_film(ID)

class Controller_Utilizator:
    utilizatorRepo = None

    def __init__(self, Utilizator_Repo):
        self.utilizatorRepo = Utilizator_Repo

    def read_file(self):
        return self.utilizatorRepo.read_file()

    def write_file(self):
        return self.utilizatorRepo.write_file()

    def write_file_comenzi(self):
        return self.utilizatorRepo.write_file_comenzi()

    def afisare_utilizatori(self):
        return self.utilizatorRepo.afisare_utilizatori()

    def add_utilizator(self, U):
        self.utilizatorRepo.add_utilizator(U)

    def update_utilizator(self, ID, nume_nou):
        return self.utilizatorRepo.update_utilizator(ID, nume_nou)

    def del_utilizator(self, ID):
        return self.utilizatorRepo.del_utilizator(ID)

    def adaugare_comanda(self, IDu, IDf):
        return self.utilizatorRepo.adaugare_comanda(IDu, IDf)