x = 1
y = 1
print("{:>4}".format("  "), end=" ")
for x in range(1, 11):
    print("{:>4}".format(x), end=" ")
print()
for x in range(1, 11):
    print("{:>4}".format(x), end=" ")
    while y <= 10:
        print("{:>4}".format(x*y), end=" ")
        y += 1
    print()
    y = 1