numbers = input()
n = (int(numbers) for numbers in numbers.split())
for i in n:
    if int(i) % 2 == 0:
        print(i, end=' ')
