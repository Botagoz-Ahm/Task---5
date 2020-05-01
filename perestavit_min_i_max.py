n = [int(s) for s in input().split()]
chislo_minimum = 0
chislo_maximum = 0
for i in range(1, len(n)):
    if n[i] > n[chislo_maximum]:
        chislo_maximum = i
    if n[i] < n[chislo_minimum]:
        chislo_minimum = i
n[chislo_minimum], n[chislo_maximum] = n[chislo_maximum], n[chislo_minimum]
print(' '.join([str(i) for i in n]))
