import math
def prikazPoStranama(linkovi,brLinkova=10):

    brojStrana=math.ceil(len(linkovi) / brLinkova)
    if (len(linkovi) < brLinkova):
        brojStrana = 1

    trenutna=1
    izlaz=False

    while izlaz==False:
        print("Ukupan broj stranica je: "+str(brojStrana))
        print("           Prikaz rezultata po strananama           ")
        print("----------------------------------------------------")
        if trenutna == brojStrana:
            for i in range((trenutna - 1) * brLinkova, len(linkovi)):
                print(linkovi[i])
        elif trenutna >= brojStrana:
            trenutna=brojStrana
            for i in range((trenutna - 1) * brLinkova, len(linkovi)):
                print(linkovi[i])
        else:
            for i in range((trenutna - 1) * brLinkova, trenutna * brLinkova):
                print(linkovi[i])
        print("----------------------------------------------------")

        tekst = ""

        if trenutna > 1:
            tekst += "Prethodna "

        pocetak = 1
        kraj = brojStrana

        if brojStrana > 10:
            kraj = 10

            if trenutna > 6:
                pocetak = trenutna - 5
                kraj = trenutna + 4

                if kraj > brojStrana:
                    pocetak = pocetak - (brojStrana - kraj)
                    kraj = brojStrana

        for i in range(pocetak, kraj+1):
            if i == trenutna:
                CYELLOW = '\033[93m'
                CEND = '\033[0m'
                tekst+= CYELLOW + str(i) + CEND+" "
            else:
                tekst+=str(i)+" "
        if trenutna<brojStrana:
            tekst+="Sledeca"
        print(tekst)
        print("          ")
        print("Za izmenu broja rezultata po stranici ukucajte I ili izaberite broj stranice")
        print("Za izlaz unesite 0")
        unos=input("Vas izbor je: ")
        if unos.isnumeric()==True:
            izbor=int(unos)
            if izbor==0:
                izlaz=True
                continue
            while True:
                if izbor>0 and izbor<=brojStrana:
                    trenutna=izbor
                    break
                else:
                    izbor1= input("Molmo Vas unesite validan broj stranice:")
                    if izbor1.isnumeric()==True:
                        izbor = int(izbor1)
                    else:
                        continue
        else:
            if unos.lower()=="sledeca":
                if trenutna<brojStrana:
                    trenutna=trenutna+1
                continue
            if unos.lower()=="prethodna":
                if trenutna>1:
                    trenutna = trenutna - 1
                continue

            if unos=="I":
                noviBrPoStr=input("Unesite zeljeni broj rezultata po strani: ")
                while True:
                    if noviBrPoStr.isnumeric()==True:
                        novo = int(noviBrPoStr)
                        if novo>0 and novo<len(linkovi):
                            brojStrana = math.ceil(len(linkovi) / novo)
                            brLinkova=novo
                        # trenutna=1
                            break
                        else:
                            brojStrana=1
                            trenutna=1
                    else:
                        noviBrPoStr=input("Unesite broj rezutata na jednoj strani: ")
                        continue
