n = list(input().split())
max = 1000
for i in range(len(n)):
    s = int(n[i])
    if (s < max) and (s > 0):
        max = s
print(max)
