from Repository.Repo import *
from Domain.Film import *
from Domain.Utilizator import *
from Control.Control import *

film_repo = Film_Repo()
film_control = Controller_Film(film_repo)
filme = film_control.read_file()

utilizator_repo = Utilizator_Repo()
utilizator_control = Controller_Utilizator(utilizator_repo)
utilizatori = utilizator_control.read_file()

def meniu_filme():
    '''
    Meniul are 5 optiuni numerotate de la 1 la 5. Daca optiunea aleasa
    nu exista se va afisa un mesaj de eroare si se va introduce o noua optiune
    pana la alegerea optiunii 5
    '''

    print(' ')
    print('1. Adaugare film')
    print('2. Actualizare pret film')
    print('3. Afisarea filmelor')
    print('4. Afisare optiuni')
    print('5. Iesire din meniu')
    print(' ')

    opt = input('Alegeti o optiune: ')
    while opt < '1' or opt > '5':
        print('Optiunea aleasa nu exista')
        opt = input('Alegeti o optiune: ')
    print(' ')

    while '5':

        if opt == '1':
            ID = int(input("ID film: "))
            while type(ID) != int:
                ID = input("ID-ul trebuie sa fie un numar")
            nume = input('Nume: ')

            an = int(input('An: '))
            while an < 0:
                an = int(input('Introduceti un an valid: '))

            scor = float(input('Scor: '))
            while scor < 0 or scor > 10:
                scor = float(input('Introduceti un scor vaild: '))

            actori = []
            nr_actori = int(input('Numar actori: '))
            while nr_actori < 0:
                nr_actori = int(input('Introduceti un numar valid de actori: '))

            for i in range(nr_actori):
                act = input('Actor:')
                actori.append(act)

            pret = float(input('Pret: '))
            while pret < 0:
                pret = float(input('Introduceti un pret vaild: '))

            F = Film(ID, nume, an, scor, actori, pret)
            film_control.add_film(F)

        if opt == '2':
            ID = int(input('ID film: '))
            pret_nou = float(input('Pret nou: '))
            while pret_nou < 0:
                pret_nou = float(input('Introduceti un pret vaild: '))

            if (film_control.update_pret(ID, pret_nou) == 1):
                print('Pret actualizat.')
            else:
                print('Nu exista acest film.')

        if opt == '3':
            for i in range (len(filme)):
               print(filme[i])

        if opt == '4':
            print(' ')
            print('1. Adaugare film')
            print('2. Actualizare pret film')
            print('3. Afisarea filmelor')
            print('4. Afisare optiuni')
            print('5. Iesire din meniu')

        if opt == '5':
            main()

        print(' ')
        opt = input('Alegeti o optiune: ')
        while opt < '1' or opt > '5':
            print('Optiunea aleasa nu exista')
            opt = input('Alegeti o optiune: ')
        print(' ')

def meniu_utilizator():
    '''
    Meniul are 5 optiuni numerotate de la 1 la 5. Daca optiunea aleasa
    nu exista se va afisa un mesaj de eroare si se va introduce o noua optiune
    pana la alegerea optiunii 5
    '''

    print(' ')
    print('1. Adaugare utilizator')
    print('2. Actualizare nume utilizator')
    print('3. Stergere utilizator')
    print('4. Afisare optiuni')
    print('5. Iesire din meniu')
    print(' ')

    opt = input('Alegeti o optiune: ')
    while opt < '1' or opt > '5':
        print('Optiunea aleasa nu exista\n')
        opt = input('Alegeti o optiune: ')

    while '5':

        # print('\nLista actuala de utilizatori:\n')
        # utilizatori = utilizator_control.afisare_utilizatori()
        # for utilizator in utilizatori:
        # print(utilizator.nume, utilizator.prenume, utilizator.comanda)
        # print(' ')

        if opt == '1':
            ID = input('ID utilizator: ')
            nume = input('Nume: ')
            prenume = input('Prenume:')
            nr_filme = int(input('Cate filme are deja comandate: '))
            comanda = []
            while nr_filme < 0:
                nr_filme = int(input('Introudceti un numar de filme deja comandate valid: '))
            for i in range(nr_filme):
                cmd = int(input('ID film: '))
                comanda.append(cmd)
            U = Utilizator(ID, nume, prenume, comanda)
            utilizator_control.add_utilizator(U)

        if opt == '2':
            ID = int(input('ID utilizator: '))
            nume_nou = input('Numele nou: ')
            if utilizator_control.update_utilizator(ID, nume_nou) == 1:
                print('Nume actualizat')
            else:
                print('Utilizatorul nu exista')

        if opt == '3':
            ID = int(input('ID utilizator: '))
            if (utilizator_control.del_utilizator(ID) == 1):
                print('Utilizator sters.')
            else:
                print('Utilizatorul nu exista')

        if opt == '4':
            print(' ')
            print('1. Adaugare utilizator')
            print('2. Actualizare nume utilizator')
            print('3. Stergere utilizator')
            print('4. Afisare optiuni')
            print('5. Iesire din meniu')

        if opt == '5':
            main()

        print(' ')
        opt = input('Alegeti o optiune: ')
        while opt < '1' or opt > '5':
            print('Optiunea aleasa nu exista\n')
            opt = input('Alegeti o optiune: ')
        print(' ')

def meniu_comenzi():
    '''
    Meniul are 6 optiuni numerotate de la 1 la 6. Daca optiunea aleasa
    nu exista se va afisa un mesaj de eroare si se va introduce o noua optiune
    pana la alegerea optiunii 6
    '''

    print('1. Comanda si afsiare pret')
    print('2. Utilizatori si comenzi')
    print('3. Filme dupa scor')
    print('4. Cautare actor')
    print('5. Afisare optiuni')
    print('6. Iesire din meniu')
    print(' ')

    opt = input('Alegeti o optiune: ')
    while opt < '0' or opt > '6':
        print('Optiunea aleasa nu exista\n')
        opt = input('Alegeti o optiune: ')
    print(' ')

    while '6':
        if opt == '1':
            for i in range (len(filme)):
               print(filme[i])
            print(' ')

            IDu = int(input('ID utilizator: '))
            s = 0
            ok = 1
            nr_filme = int(input('Cate filme doriti: '))

            for i in range(nr_filme):
                IDf = int(input('ID film: '))
                f = film_control.cautare_film(IDf)
                if f == -1:
                    print('Filmul nu este disponibil.')
                else:
                    s = s + f
                    if utilizator_control.adaugare_comanda(IDu, IDf) == 0:
                        ok = 0

            if ok == 1:
                print('Aveti de platit: ', s)
            else:
                print('Utilizatorul nu exista.')

        if opt == '2':
            for i in range (len(utilizatori)):
                print(utilizatori[i])

        if opt == '3':
            scor_minim = float(input('Scorul minim: '))
            while scor_minim > 10 or scor_minim < 0:
                scor_minim = float(input('Introduceti un alt scor minim: '))
            lista = film_control.cautare_scor(scor_minim)
            for i in range(len(lista)):
                print(lista[i])

        if opt == '4':
            nume_actor = input('Nume actor: ')
            lista = film_control.cautare_actor(nume_actor)
            if not lista:
                print("Actorul nu joaca nicaieri")
            else:
                for i in range(len(lista)):
                    print("Titlu: ", lista[i].nume, " An: ", lista[i].an, " Scor: ", lista[i].scor, " Actori: ",
                          lista[i].actori, " Pret: ", lista[i].pret)

        if opt == '5':
            print(' ')
            print('0. Citeste din fisier')
            print('1. Comanda si afsiare pret')
            print('2. Utilizatori si comenzi')
            print('3. Filme dupa scor')
            print('4. Cautare actor')
            print('5. Afisare optiuni')
            print('6. Iesire din meniu')

        if opt == '6':
            main()

        print(' ')
        opt = input('Alegeti o optiune: ')
        while opt < '0' or opt > '6':
            print('Optiunea aleasa nu exista\n')
            opt = input('Alegeti o optiune: ')
        print(' ')

def main():
    '''
    Meniul are trei optiuni numerotate de la 1 la 4. Daca optiunea aleasa
    nu exista se va afisa un mesaj de eroare si se va introduce o noua optiune
    pana la alegerea optiunii 4
    '''

    print('1. Meniu utilizator')
    print('2. Meniu filme')
    print('3. Meniu comenzi')
    print('4. Exit')
    print(' ')

    opt = input('Alegeti o optiune: ')
    while opt < '1' or opt > '4':
        print('Optiunea aleasa nu exista\n')
        opt = input('Alegeti o optiune: ')

    while '4':
        if opt == '1':
            meniu_utilizator()

        if opt == '2':
            meniu_filme()

        if opt == '3':
            meniu_comenzi()

        if opt == '4':
            utilizator_control.write_file()
            film_control.write_file()
            utilizator_control.write_file_comenzi()
            break

        opt = input('Alegeti o optiune: ')
        while opt < '1' or opt > '4':
            print('Optiunea aleasa nu exista\n')
            opt = input('Alegeti o optiune: ')

print(' ')
main()