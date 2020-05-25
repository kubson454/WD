with open('zad2.txt', 'w') as writer:
    lista = []
    for x in range(1,20):
        if x%4==0:
           lista.append(x)
    writer.write(str(lista))
    
with open("zad2.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")