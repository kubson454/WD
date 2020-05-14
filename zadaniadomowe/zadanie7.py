while True:

    print ("podaj liczbe: ")
    liczba = input()
    liczba = int(liczba)
    x = liczba*liczba
    print ("potega z liczby",liczba ,"wynosi: ",x)
    print ("czy liczymy dalej y/n: ")

    y = input()

    if y == 'n' :
        print ("koniec programu")   
        break 
