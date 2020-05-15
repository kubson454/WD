a = input("Podaj liczbe, aby obliczyc sume jej cyfr\n")
sumaCyfr = 0
for cyfra in str(a):

   sumaCyfr += int(cyfra)

print(sumaCyfr)