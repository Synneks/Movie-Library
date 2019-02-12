from Domain.Film import Film
from Domain.Utilizator import Utilizator

class Film_Repo:
    lista_filme = [Film]

    def __init__(self):
        self.lista_filme = []

    def read_file(self):
        with open('D:\FAC\PyCharm\Lab5\Film.txt', 'r') as f:
            line = f.readline().strip()
            while line != "":
                t = line.split(",")
                t[4] = t[4].strip('[')
                t[4] = t[4].strip(']')
                t[4] = t[4].strip("'")
                l = t[4].split(';')
                new = Film(int(t[0]), t[1], int(t[2]), float(t[3]), l, float(t[5]))
                self.add_film(new)
                line = f.readline().strip()
        return self.lista_filme

    def write_file(self):
        with open('D:\FAC\PyCharm\Lab5\Film.txt', 'w') as f:
            for i in range(0, len(self.lista_filme)):
                f.write(str(self.lista_filme[i].ID) + ',')
                f.write(str(self.lista_filme[i].nume) + ',')
                f.write(str(self.lista_filme[i].an) + ',')
                f.write(str(self.lista_filme[i].scor) + ',')
                f.write(str(self.lista_filme[i].actori) + ',')
                f.write((str(self.lista_filme[i].pret)) + '\n')

    def add_film(self, film):
        '''
        Adauga filmul la lista de filme.
        :param film:
        :return:
        '''
        self.lista_filme.append(film)

    def afisare_filme(self):
        '''
        Afiseaza toate filmele
        :return:
        '''
        return self.lista_filme

    def update_pret(self, ID, pret_nou):
        '''
        Actualizeaza pretul filmului dupa ce il cauta in functie de nume.
        :param nume:
        :param pret_nou:
        :return:
        '''
        for i,film in enumerate(self.lista_filme):
            if ID == int(film.ID):
                film.pret = pret_nou
                return 1
        return 0

    def cautare_scor(self, scor_minim):
        '''
        Compara fiecare film din lista cu scorul minim. Daca gaseste un film cu un scor mai mare
        il adauga in lista.
        :param scor_minim:
        :return:
        '''
        lista = []
        for i,film in enumerate(self.lista_filme):
            if scor_minim < film.scor:
                lista.append(film)
        return lista

    def cautare_actor(self, nume_actor):
        '''
        Cauta in fiecare lista cu actori ai unui film un nume care sa fie la fel cu cel cautat. Daca
        exista un astfel de actor,adauga in lista filmul in care joaca actorul.
        :param nume_actor:
        :return:
        '''
        lista = []
        for i in range (len(self.lista_filme)):
            for j in range (len(self.lista_filme[i].actori)):
                if nume_actor == self.lista_filme[i].actori[j]:
                    lista.append(self.lista_filme[i])
        return lista

    def cautare_film(self, ID):
        '''
        Cauta in lista de filme un film cu acelasi nume cu cel cautat, si returneaza pretul acelui film.
        :param filmul:
        :return:
        '''
        for i in range (len(self.lista_filme)):
            if ID == self.lista_filme[i].ID:
                return self.lista_filme[i].pret
        return -1

def Film_Repo_test():
    film_repo = Film_Repo()
    film = Film(32,'Film',2,8.5,["John","Pete"],50)
    film_repo.add_film(film)
    return film_repo

def add_film_test():
    film_repo = Film_Repo_test()
    film = Film(45,"film",2,5,["el"],1)
    film_repo.add_film(film)
    assert len(film_repo.lista_filme) == 5
    print ('Film add functioneaza')

def cautare_film_test():
    film_repo = Film_Repo_test()
    pret = film_repo.cautare_film(32)
    assert pret == 50
    print ('Film cautare functioneaza')

#cautare_film_test()
#add_film_test()

class Utilizator_Repo:
    lista_utilizatori = [Utilizator]

    def __init__(self):
        self.lista_utilizatori = []

    def read_file(self):
        with open('D:\FAC\PyCharm\Lab5\Oameni.txt', 'r') as f:
            line = f.readline().strip()
            while line != "":
                t = line.split(",")
                t[3] = t[3].strip('[')
                t[3] = t[3].strip(']')
                t[3] = t[3].strip("'")
                l = t[3].split(';')
                new = Utilizator(t[0], t[1], t[2], l)
                self.add_utilizator(new)
                line = f.readline().strip()
        return self.lista_utilizatori

    def write_file(self):
        with open('D:\FAC\PyCharm\Lab5\Oameni.txt', 'w') as f:
            for i in range(0, len(self.lista_utilizatori)):
                f.write(str(self.lista_utilizatori[i].ID) + ',')
                f.write(str(self.lista_utilizatori[i].nume) + ',')
                f.write(str(self.lista_utilizatori[i].prenume) + ',')
                f.write(str(self.lista_utilizatori[i].comanda) + '\n')

    def write_file_comenzi(self):
        with open('D:\FAC\PyCharm\Lab5\Comenzi.txt', 'a') as f:
            for i in range(0, len(self.lista_utilizatori)):
                f.write(str(self.lista_utilizatori[i].ID) + ',')
                f.write(str(self.lista_utilizatori[i].nume) + ',')
                f.write(str(self.lista_utilizatori[i].prenume) + ',[')
                for j in range(len(self.lista_utilizatori[i].comanda)):
                    f.write(str(self.lista_utilizatori[i].comanda[j]) + ',')
                f.write(']\n')

    def afisare_utilizatori(self):
        return self.lista_utilizatori

    def add_utilizator(self, utilizator):
        '''
        Adauga utilizatorul la lista de utilizatori.
        '''
        self.lista_utilizatori.append(utilizator)

    def update_utilizator(self, ID, nume_nou):
        '''
        Actualizeaza numele utilizatorului dupa ce il cauta in functie de nume si prenume.
        '''
        for i,utilizator in enumerate(self.lista_utilizatori):
            if ID == int(utilizator.ID):
                utilizator.nume = nume_nou
                return 1
        return 0

    def del_utilizator(self, ID):
        '''
        Sterge utilizatorul dupa ce il cauta in functie de nume si prenume.
        :param nume:
        :param prenume:
        :return:
        '''
        for i,utilizator in enumerate(self.lista_utilizatori):
            if ID == int(utilizator.ID):
                del self.lista_utilizatori[i]
                return 1
        return 0

    def adaugare_comanda(self, IDu, IDf):
        '''
        Preia filmul pe care utilizatorul il comanda si il adauga la lista de comenzi ale acestuia.
        :param nume:
        :param prenume:
        :param filmul:
        :return:
        '''
        ok = 0
        for i,utilizator in enumerate(self.lista_utilizatori):
            if IDu == int(utilizator.ID):
                utilizator.comanda.append(IDf)
                ok = 1
                break
        if ok == 1:
            return 1
        else:
            return 0

def Utilizator_Repo_test():
    utilizator_repo =Utilizator_Repo()
    utilizator = Utilizator(12,'Popa','Ion',[])
    utilizator_repo.add_utilizator(utilizator)
    return utilizator_repo

def add_utilizator_test():
    utilizator_repo = Utilizator_Repo_test()
    utilizator = Utilizator(13,'Masca','Dan',[])
    utilizator_repo.add_utilizator(utilizator)
    assert len(utilizator_repo.lista_utilizatori)==5
    print('Utilizator add functioneaza.')

def update_utilizator_test():
    utilizator_repo = Utilizator_Repo_test()
    utilizator = Utilizator(13,'Masca', 'Dan', [])
    utilizator_repo.add_utilizator(utilizator)
    ID = 13
    nume_nou = 'Morar'
    utilizator_repo.update_utilizator(ID, nume_nou)
    assert nume_nou == utilizator_repo.lista_utilizatori[4].nume
    print('Utilizator update functioneaza')

def del_utilizator_test():
    utilizator_repo = Utilizator_Repo_test()
    utilizator = Utilizator(12,'Masca','Dan',[])
    utilizator_repo.add_utilizator(utilizator)
    utilizator_repo.del_utilizator(12)
    assert len(utilizator_repo.lista_utilizatori)==4
    print('Utilizator del functioneaza')

#add_utilizator_test()
#update_utilizator_test()
#del_utilizator_test()
