n = [int(i) for i in input().split()]
for i in range(1, len(n), 2):
    n[i - 1], n[i] = n[i], n[i - 1]
print(' '.join([str(i) for i in n]))
