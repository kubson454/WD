print ("podaj a:")
a = input()
a = int(a)

print ("podaj b:")
b = input()
b = int(b)

print ("podaj c:")
c = input()
c= int(c)

if (a>0 and a<=10):
    print("a nazlezy do przedzialu (0;10>")
    if (a>b):
        print ("a>b")
    elif (b>c):
        print ("b>c")
    elif (a==b and b==c):
        print ("liczby sa rowne")
    else:
        print ("c ma najwieksza wartosc")
else:
        print ("a nie zawiera siew przedziale (0;10>")