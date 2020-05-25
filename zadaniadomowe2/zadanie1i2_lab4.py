import sys


# tworzymy liste
lista = []
for x in range(1,20):
    if x%4==0:
        lista.append(x)

# otwieramy plik do dopisywania
plik=open("zad1.txt","a+")

# zapisujemy
plik.writelines(str(lista))

# zamykamy
plik.close()


with open("zad1.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")