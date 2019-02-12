class Utilizator:
    ID = 0
    nume = ''
    prenume = ''
    comanda = []

    def __init__(self, ID, nume, prenume, comanda):
        self.ID = ID
        self.nume = nume
        self.prenume = prenume
        self.comanda = comanda

    def __str__(self):return "<ID:%s nume:%s prenume:%s comanda:%s"%(str(self.ID), self.nume, self.prenume, self.comanda)


def test():
    utilizator = Utilizator(1,"nume","prenume",["It"])
    return utilizator

def test_init():
    utilizator = test()
    assert utilizator.ID == 1
    assert utilizator.nume == 'nume'
    assert utilizator.prenume == 'prenume'
    assert utilizator.comanda == 'It'
    print ("Succes ut")

#test_init()

