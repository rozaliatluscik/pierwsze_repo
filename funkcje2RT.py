liczba=899

def dzialanie():
    liczba=567567

print(liczba)


def rysujProstokat(dlugosc, szerokosc, element=4):
    for i in range(dlugosc):
        for j in range(szerokosc):
            print(element, end='')
        print()

rysujProstokat(2,3)
rysujProstokat(3,5,'*')


def gwiazdki(liczbaGwiazdek):
    if liczbaGwiazdek > 0:
        print("*")
        gwiazdki(liczbaGwiazdek-1)

gwiazdki(5)


lista=[1,2,3,4,5]
def sumowanie(listaLiczb):
    if len(listaLiczb)>0:
        return listaLiczb[0]+sumowanie(listaLiczb[1:])
    else:
        return 0

wynik=sumowanie(lista)
print(wynik)


lista=[1,2,3,4,5]
def mnozenie(listaLiczb):
    if len(listaLiczb)>0:
        return listaLiczb[0]*mnozenie(listaLiczb[1:])
    else:
        return 1

wynik=mnozenie(lista)
print(wynik)


Zadanie 1
lista=[1,2,3,4,5]
def ostatni(listaLiczb):
    if len(listaLiczb)>1:
        return ostatni(listaLiczb[1:])
    else:
        return listaLiczb[0]

wynik=ostatni(lista)
print(wynik)


Zadanie 4
def dlugosc(listaLiczb):
    if listaLiczb:
        return 1+dlugosc(listaLiczb[1:])
    else:
        return 0

lista=[1,2,3,4,5]
wynik=dlugosc(lista)
print(wynik)


Zadanie 3
def maksymalna(listaLiczb, zapamietana):
    if len(listaLiczb)>0:
        if listaLiczb[0]>zapamietana:
            zapamietana=listaLiczb[0]
        return maksymalna(listaLiczb[1:], zapamietana)
    else:
        return zapamietana

lista=[5,6,7,8,9,10]
wynik=maksymalna(lista, lista[0])
print(wynik)

Zadanie 6
def czynaliscie(listaLiczb, do_sprawdzenia):
    if len(listaLiczb)>0:
        if listaLiczb[0] == do_sprawdzenia:
            return "TAK"
        else:
            return czynaliscie(listaLiczb[1:], do_sprawdzenia)
    else:
        return "NIE"

lista=[1,2,3,4,5]
wynik=czynaliscie(lista, 5)
print(wynik)


listeczka = [51,23,44,67,90]
print(listeczka)

listunia = [224,2141,5436,232]
print(listunia)
