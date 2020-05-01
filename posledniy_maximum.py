n = [int(i) for i in input().split()]
maximum = max(n)
ind = 0
for i in range(1, len(n)):
    if n[i] == maximum:
        ind = i
print(maximum, ind)
