myRange = int(input())
for n in range(myRange):
    print("+___", end=" ")
print()
for n in range(myRange):
    print("|%s /" % (n + 1), end=" ")
print()
for n in range(myRange):
    print("|__\\", end=" ")
print()
for n in range(myRange):
    print("|   ", end=" ")
print()
