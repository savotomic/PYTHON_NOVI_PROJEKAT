 # -*- coding: utf-8 -*-
class Cvor:
    def __init__(self, stranica=None):
        self._naziv=stranica

    def sadrzaj(self):
        return self._naziv

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return str(self._naziv)

class Grana:
    def __init__(self, pocetana,krajnja,link):
        self._pocetak = pocetana
        self._kraj = krajnja
        self._grana = link

    def suprotni_cvor(self, v): #vraca cvor koji se nalazi na drugoj strani grane
        if not isinstance(v, Cvor):
            raise TypeError('v mora biti instanca klase Cvor')
        return self._kraj if v is self._pocetak else self._pocetak


    def __hash__(self):  # omogućava da Edge bude ključ mape
        return hash((self._pocetak, self._kraj))


class Graph:

    def __init__(self):
        self._graneKojeIzlaze= {}
        self._graneKojeUlaze = {}

    def _validate_vertex(self, cvor):   #proverava da li je dat objekat cvor grafa
        if not isinstance(cvor, Cvor):
            raise TypeError('Objekat nije klase Cvor')
        if cvor not in self._graneKojeIzlaze:
            raise ValueError('Dati cvor ne pripada grafu.')




    def cvorovi_grafa(self):  #vraca sve cvorove grafa

        return self._graneKojeIzlaze.keys()




    def grana_grafa(self, u, v):    #vraca granu za date cvorove

        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._graneKojeIzlaze[u].get(v)



    def ulazne_grane_cvora(self, v):  # vraca sve grane koje ulaze u trazeni cvor
                                    # ovo ce nam pomoci kod rangiranja
        self._validate_vertex(v)
        return self._graneKojeUlaze[v].values()

    def dodaj_cvor(self, starnica=None): #dodaje novi cvor u graf
                                        # ukoliko cvor vec postoji vraca taj cvor
        postoji = False
        for cvor in self.cvorovi_grafa():
            if cvor.sadrzaj() == starnica:
                postoji = True               # provera da li cvor postoji u grafu
                return cvor
        if not postoji:
            v = Cvor(starnica)
            self._graneKojeIzlaze[v] = {}
            self._graneKojeUlaze[v] = {}
        return v

    def dodaj_granu(self, pocetak, kraj, link=None): #dodavanje grane u graf

        if self.grana_grafa(pocetak, kraj) is not None:
            return None

        else:
            e =  Grana(pocetak, kraj, link)
            self._graneKojeIzlaze[pocetak][kraj] = e
            self._graneKojeUlaze[kraj][pocetak] = e
        return e