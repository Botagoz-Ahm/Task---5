n = input()
n = [int(i) for i in n.split()]
for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        print(n[i], end=' ')
