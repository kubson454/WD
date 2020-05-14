print ("ile liczb bedzie miala lista:  ")
liczba = input()
liczba = int(liczba)
lista = []
i = 0
while i < liczba: 
    i+=1    
    print ("podaj liczbe: ")
    a = input()
    a = int(a)
    lista.append(int(a))

print("elementy listy:",lista)