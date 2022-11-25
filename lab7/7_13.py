def od(n):
    a = n // 1000
    m = n % 1000
    b = m // 100
    k = m % 100
    c = k // 10
    d = k % 10
    if c == d or c == a or c == b or d == a or d == b or a == b:
        return ''
    else:
        return "{} ".format(n)


a, b = map(int, input().split())
while a <= b:
    print(od(a), end="")
    a += 1
