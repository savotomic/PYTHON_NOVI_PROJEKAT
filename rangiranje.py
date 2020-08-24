def rang(podaci,graf):
    rangovi = {}
    for key in podaci.keys():
        rang = podaci[key] * 1.5
        linkovi = graf.ulazne_grane_cvora(key)
        rang += len(linkovi) * 1.35
        for link in linkovi:
            prekoputa = link.suprotni_cvor(key)
            if prekoputa in podaci.keys():
                rang += podaci[prekoputa] * 1.2
        rang = round(rang, 2)
        rangovi[key.sadrzaj()] = rang
    return rangovi


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].rang < arr[j + 1].rang:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]