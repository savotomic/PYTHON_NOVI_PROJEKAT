from ParsiranjeHTML import *
from Trie import *
from parsiranje import *
from Set import *
from rangiranje import *

logickeOperacije = ["and","or","not"]

def obicanUpit(upit,graf,trie):              #funkcija sluzi da se pretraze reci u zadatim html stranicama
    if (len(upit) > 0):
        reci = upit.split(" ")
        if (len(reci) > 1 and (reci[1].lower() in logickeOperacije) and len(reci) == 3):
            rangiraj = logickiupit(upit, graf,trie)   #ovde pozivamo pretragu i rangiranje za logicki upit,ukoliko su ispunjeni uslovi
            return rangiraj
        s = Set()
        for rec in reci:
            if(rec.lower() in logickeOperacije):
                print("Greska pri unosu!")
                return None
        for i in range(len(reci)):      #omoguca se pretraga vise reci odjednom
            print("Pronalazenje reci " + str(reci[i]) + "...")
            novi_recnik = trie.find_prefix(reci[i])
            rangirani_recnik=rang(novi_recnik,graf)
            reci[i]=rangirani_recnik
        pomocna=reci[0]

        if len(reci)==1:
            return reci[0]

        for i in range(1,len(reci)):  #vrsi se unija svih pretraznih reci i dobija se konacni rang pretrage
            recnikOR=s.unija(pomocna, reci[i])
            pomocna=recnikOR

        return pomocna
    else:
        print("Morate uneti neki unos.")
        return None


def logickiupit(upit,graf,trie):
    s=Set()
    reci = upit.split(' ')
    if (reci[0].lower() in logickeOperacije) or (reci[2].lower() in logickeOperacije):
        print("GREŠKA!!! Molimo vas da unesete upit u odgovarajućoj formi!")
        print("Primer logičkog upita: java AND python.")
        return None
    prva_rec = trie.find_prefix(reci[0])
    druga_rec = trie.find_prefix(reci[2])
    if prva_rec == 0 and druga_rec == 0:
        print("Nema rezultata pretrage.")
        return None
    rangZaPrvuRec = rang(prva_rec, graf)
    rangZaDruguRec = rang(druga_rec, graf)

    if(reci[1].lower() == "and"):
        krajnjiRang = s.presek(rangZaPrvuRec,rangZaDruguRec)
        return krajnjiRang

    if (reci[1].lower() == "or"):
        krajnjiRang = s.unija(rangZaPrvuRec, rangZaDruguRec)
        return krajnjiRang

    if (reci[1].lower() == 'not'):
        krajnjiRang = s.komplement(rangZaPrvuRec, rangZaDruguRec)
        return krajnjiRang




