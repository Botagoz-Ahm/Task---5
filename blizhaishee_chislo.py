n = int(input())
m = map(int, input().split())
x = int(input())
print(min(m, key=lambda a: abs(a - x)))
