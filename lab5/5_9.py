a, b, c, d = map(int, input().split())
if a > b:a,b = b, a
if c > d:c,d = d, c

n = 0
e = 0
array = [a * c]
for i in range(a, b+1):
    for j in range(c, d+1):
        e = i * j
        n = 0
        chk = True
        while n < len(array):
            if e != array[n]:
                n = n + 1
                continue
            else:
                n = n+1
                chk = False
        if chk:array.append(e)

print(len(array))
