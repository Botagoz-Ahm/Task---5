A = int(input())
B = int(input())
if A < B:
    for myRange in range(A, B + 1):
        print(myRange, end=' ')
elif A > B:
    for myRange in range(A, B - 1, -1):
        print(myRange, end=' ')
else:
    print(A or B)
