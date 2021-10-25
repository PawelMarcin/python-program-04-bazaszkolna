"""Program Baza Szkolna.
Program wczytuje z pliku baze danych o klasach, wychowawcach, nauczycielach,
uczniach i przedmiotach.
Program zwraca imie i nazwisko wychowacy oraz imiona i nazwiska uczniow klasy
jesli w wywolaniu podano nr klasy (oddzialu).
Jesli w wywolaniu podano imie i nazwisko program zwraca:
    - imiona i nazwiska uczniow jesli podano dane wychowawcy
    - imiona i nazwiska wychowawcow jesli podano dane nauczyciela
    - lekcje i imiona i nazwiska nauczycieli prowadzacych lekcje jesli podano
      dane ucznia.
"""

import sys

"""------------------------------------"""

"""  definicje klas  """


class Osoba:
    def __init__(self):
        self.status = ''
        self.name = ''
        self.klasa = ''
        self.przedmiot = ''

    def uzupelnij_oddzialy(self):

        dodaj_nowy_oddzial = False

        # funkcja (stat) to uczen
        if self.status == 'uczen':
            # wczytanie klasy do ktorej uczen jest przypisany
            for i in oddzialy:
                if i['nr'] == '':
                    i['nr'] = self.klasa
                    i['uczniowie'].append(self.name)
                    dodaj_nowy_oddzial = False
                    break
                elif i['nr'] == self.klasa:
                    i['uczniowie'].append(self.name)
                    dodaj_nowy_oddzial = False
                    break
                else:
                    dodaj_nowy_oddzial = True
            if dodaj_nowy_oddzial:
                new_oddzial = {'nr': self.klasa, 'wychowawca': '', 'przedmioty': {}, 'uczniowie': []}
                new_oddzial['uczniowie'].append(self.name)
                oddzialy.append(new_oddzial)
        elif self.status == 'wychowawca':
            for i in oddzialy:
                if i['nr'] == '':
                    i['nr'] = self.klasa
                    i['wychowawca'] = self.name
                    dodaj_nowy_oddzial = False
                    break
                elif i['nr'] == self.klasa:
                    i['wychowawca'] = self.name
                    dodaj_nowy_oddzial = False
                    break
                else:
                    dodaj_nowy_oddzial = True
            if dodaj_nowy_oddzial:
                new_oddzial = {'nr': self.klasa,
                               'wychowawca': self.name,
                               'przedmioty': {},
                               'uczniowie': []}
                oddzialy.append(new_oddzial)
                # dodaj_nowy_oddzial = False
        elif self.status == 'nauczyciel':
            for i in oddzialy:
                # lista klas/oddzialow jest pusta:
                if i['nr'] == '':
                    i['nr'] = self.klasa
                    i['przedmioty'].update({self.przedmiot: self.name})
                    dodaj_nowy_oddzial = False
                    break
                # klasa z listy nauczyciela jest na liscie
                # klas/oddzialow:
                elif i['nr'] == self.klasa:
                    i['przedmioty'].update({self.przedmiot: self.name})
                    dodaj_nowy_oddzial = False
                    break
                # klasy z listy nauczyciela nie ma na liscie
                # klas/oddzialow (lista klas/oddzialow nie jest pusta)
                else:
                    # konicznosc dodania nowej pozycji do listy
                    # klas/oddzialow
                    dodaj_nowy_oddzial = True
            # dodawanie nowej pozycji do listy klas/oddzialow
            if dodaj_nowy_oddzial:
                new_oddzial = {'nr': self.klasa,
                               'wychowawca': '',
                               'przedmioty': {self.przedmiot: self.name},
                               'uczniowie': []}
                oddzialy.append(new_oddzial)
                # dodaj_nowy_oddzial = False

    def zapisz_osobe(self):
        self.status = wejscie
        self.name = input()
        ktos = {'nazwa': self.name, 'status': wejscie}
        osoby.append(ktos)
        if wejscie == 'uczen':
            self.klasa = input()
            uczen = {'nazwa': self.name, 'klasa': self.klasa}
            uczniowie.append(uczen)
            # obsluga listy klas/oddzialow (self.name, self.klasa)
            self.uzupelnij_oddzialy()
        elif wejscie == 'nauczyciel':
            self.przedmiot = input()
            self.klasa = input()
            klasy = []
            while True:
                if self.klasa:
                    klasy.append(self.klasa)
                    # obsluga listy klas/oddzialow (self.przedmiot, self.klasa)
                    self.uzupelnij_oddzialy()
                    self.klasa = input()
                else:
                    break
            nauczyciel = {'nazwa': self.name, 'przedmiot': self.przedmiot,
                          'klasy': klasy}
            nauczyciele.append(nauczyciel)
        elif wejscie == 'wychowawca':
            self.klasa = input()
            klasy = []
            while True:
                if self.klasa:
                    klasy.append(self.klasa)
                    # obsluga listy klas/oddzialow (self.klasa)
                    self.uzupelnij_oddzialy()
                    self.klasa = input()
                else:
                    break
            wychowawca = {'nazwa': self.name, 'klasy': klasy}
            wychowawcy.append(wychowawca)

    def wypisz_klase(self):
        self.name = wejscie
        for i in oddzialy:
            if i['nr'] == self.name:
                print('Klasa:')
                print('\t', i['nr'])
                print('Wychowawca:')
                print('\t', i['wychowawca'])
                print('Uczniowie:')
                for j in i['uczniowie']:
                    print('\t', j)

    def wypisz_osobe(self):
        self.name = wejscie
        for i in osoby:
            if i['nazwa'] == self.name:
                self.status = i['status']
                print(self.status + ': ' + self.name)
                if self.status == 'uczen':
                    for i in uczniowie:
                        if i['nazwa'] == self.name:
                            for j in oddzialy:
                                if j['nr'] == i['klasa']:
                                    for k, v in j['przedmioty'].items():
                                        print('\t', k, ':', '\t', v)
                elif self.status == 'nauczyciel':
                    for i in nauczyciele:
                        if i['nazwa'] == self.name:
                            for j in i['klasy']:
                                for k in oddzialy:
                                    if k['nr'] == j:
                                        print('\t',
                                              'Klasa:', j, '\t',
                                              'Wychowawca:', k['wychowawca'])
                elif self.status == 'wychowawca':
                    for i in wychowawcy:
                        if i['nazwa'] == self.name:
                            for j in i['klasy']:
                                for k in oddzialy:
                                    if k['nr'] == j:
                                        print('\t', 'Klasa', j, ':')
                                        for n in k['uczniowie']:
                                            print('\t', '\t', n)


"""  koniec definicji klas  """

osoba = Osoba()

# lista slownikow osoby() - imie i nazwisko oraz status/funkcja:
osoby = []
# lista slownikow uczniowie() - imie i nazwisko oraz klasa:
uczniowie = []
# lista slownikow nauczyciele() - imie i nazwisko, przedmiot nauczany
# oraz lista klas:
nauczyciele = []
# lista slownikow wchowawcy() - imie i nazwisko oraz lista klas:
wychowawcy = []

oddzial = {'nr': '', 'wychowawca': '', 'przedmioty': {}, 'uczniowie': []}
oddzialy = [oddzial, ]

while True:
    wejscie = input()
    if wejscie == 'koniec':
        break
    else:
        osoba.zapisz_osobe()

wejscie = sys.argv[1]

# TODO dodac chociaz szczatkowa obsluge blednego argumentu wejsciowego

if len(wejscie) == 2:
    # wypisac wychowace klasy oraz uczniow
    osoba.wypisz_klase()
else:
    # wypisac dane dla podanego nazwiska zalezne od funkcji/statusu "nazwiska"
    osoba.wypisz_osobe()

# TODO przepisac program z inna struktura stryktury oddzialy - tak aby byla
#  slownikiem slownikow
