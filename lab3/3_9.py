N = int(input())
count = 0
i = 0

while count < N:
    i += 1
    if i % 2 > 0 and i % 3 > 0 and i % 5 > 0:
        count += 1
        print(i, end=" ")
