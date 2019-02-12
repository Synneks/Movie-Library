class Film:
    ID = 0
    nume = ''
    an = ''
    scor = ''
    actori = []
    pret = 0

    def __init__(self, ID, nume, an, scor, actori, pret):
        self.ID = ID
        self.nume = nume
        self.an = an
        self.scor = scor
        self.actori = actori
        self.pret = pret

    def __str__(self):return "<ID:%s nume:%s an:%s scor:%s actori:%s pret:%s>" % (self.ID, self.nume, self.scor, self.an, self.actori, self.pret)


def test():
    film = Film(1,"nume",1,8.5,["John","Pete"],50)
    return film

def test_init():
    film =  test()
    assert film.ID == 1
    assert film.nume == 'nume'
    assert film.an == 1
    assert film.scor == '8.5'
    assert film.actori == ['John',"Pete"]
    assert film.pret == 50
    print ('Succes film')

#test_init()