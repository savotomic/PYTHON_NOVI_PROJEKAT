from time import time

from parsiranje import *
from Trie import *
from ParsiranjeHTML import *
from pretraga import *
from graf import Graph
from paginacija import *
from rangiranje import *

class Pomocni:               #ova klasa nam sluzi da lakse izvrsimo sortiranje i prikaz rezultata
    def __init__(self,ulazniLink,ulazniRang):
        self.link=ulazniLink
        self.rang=ulazniRang
    def __str__(self):
        return str(self.link) +" Rang: "+ str(self.rang)

if __name__ == '__main__':
    running = True
    userInput = None
    graf = Graph()
    rezultat=[]

    while running:
        print("")
        print("*********************")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiraj HTML fajl")
        print("2 - Parsiraj uneti HTML fajl")
        print("3 - Pretrazi HTML fajl")
        print("4 - Prikaz rezultata po stranama")
        print("5 - Prikaz rezultata")
        userInput = input("Izaberi opciju: ")
        if userInput == "0":
            running = False

        if userInput == "1":
            startTime = time()
            print("Vrsi se parsiranje...")
            path = "C:\\Users\\ASsoft\\Desktop\\novi_projekat_python\\novi_projekat_python\\python-2.7.7-docs-html"
            root = TrieNode('*', path)
            trie=Trie(root)
            parsiraj(path,graf,trie)
            endTime = time()
            vreme = endTime - startTime
            print("Vreme ucitavanja HTML fajla: " + str(vreme) + " sekundi")

        if userInput == "2":

            path = str(input('Unesi putanju za HTML fajl: '))
            root = TrieNode('*', path)
            trie = Trie(root)
            startTime = time()
            print("Vrsi se parsiranje...")
            recnik = parsiraj(path,graf,trie)
            endTime = time()
            vreme = endTime - startTime
            print("Vreme ucitavanja unetog HTML fajla: " + str(vreme) + " sekundi")

        if userInput == "3":
            if graf._graneKojeIzlaze=={}:
                print("Molimo vas prvo izabrite opciju 1 ili 2!")
                continue

            print("Ako zelite obicnu pretragu, unesite reci koje zelite da pretrazite")
            print("Ako zelite logicku pretragu. unesite kao u primeru. Primer: rec operand rec. Operandi su : and,or i not")
            unos = str(input("Pretraga: "))
            startTime = time()

            rezultat=obicanUpit(unos,graf,trie)
            if rezultat==None:
                print("Nema rezultata za datu pretragu!")
                continue

            endTime = time()
            vreme = endTime - startTime
            print("Vreme pronalazenja unosa: " + str(vreme) + " sekundi")

        if userInput == "4":
            zaSortiranje = []
            br = 1
            if (rezultat != None):
                for key, value in rezultat.items():
                    item = Pomocni(key, value)
                    zaSortiranje.append(item)

            bubble_sort(zaSortiranje)
            prikazPoStranama(zaSortiranje)

        if userInput == "5":
            zaSortiranje = []
            br = 1
            if (rezultat != None):
                for key, value in rezultat.items():
                    item = Pomocni(key, value)
                    zaSortiranje.append(item)

            bubble_sort(zaSortiranje)
            for i in range(len(zaSortiranje)):
                print(zaSortiranje[i])