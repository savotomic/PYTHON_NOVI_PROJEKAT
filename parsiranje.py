from ParsiranjeHTML import *
from graf import *
from trie import TrieNode, Trie

def parsiraj(path, graf, trie1):        #na osnovu ove metode se izgradjuju graf i trie
    parser = Parser()                   #u nasem slucaju trie ce sadrzati objekte klase Cvor
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                putanja = os.path.join(subdir, file)
                cvor = graf.dodaj_cvor(putanja)
                linkovi, reci = parser.parse(putanja)
                for rec in reci:
                    trie1.add(rec.lower(), cvor)
                for link in linkovi:
                    cvor1 = graf.dodaj_cvor(link)
                    graf.dodaj_granu(cvor, cvor1, link)



