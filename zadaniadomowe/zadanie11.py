p = (" ")
o = ("o")
wys = int(input("Podaj wysokosc od 3 do 9: "))
while (wys > 9 or wys < 3):#wystarczy zwiekszyc zakres zamaist 9 lub wprowadzic zmienna dla nie ograniczenia wielkosci diamentu
    wys = int(input("Podaj wysokosc od 3 do 9: "))
   
if (wys%2==0):
    i=1
    while i < (wys-1)/2:
        p+=" "
        i+=1 
   
    i=1
    while i < wys/2+1:
        print(p + o)
        "\n"
        o+="oo"
        p=p[:-1]
        i+=1 

    i=wys-1
    while i > wys/2-1:
        o=o[:-2]
        print(" " + p + o)
        "\n"
        p+=" "
        i-=1 
else:
    i=1
    while i < (wys-1)/2:
        p+=" "
        i+=1 
   
    i=1
    while i < (wys-1)/2+1:

        print(p + o)
        "\n"
        o+="oo"
        p=p[:-1]
        i+=1 

    i=wys
    while i > wys/2:
        print(p + o)
        "\n"
        p+=" "
        o=o[:-2]

        i-=1 