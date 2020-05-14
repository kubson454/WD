print ("podaj od jakiej liczby: ")
od = input()
od = int(od)

print ("podaj do jakiej: ")
do = input()
do = int(do)

for i in range(od,do):
    i = int(i)
    i+=1
    if i%5==0:
        print ("liczba:",i)