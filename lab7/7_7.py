def gcd(a, b):
    if b > a:
        b, a = a, b
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
res = 1

for i in range(1, N+1):
    res = lcm(res, i)

print(res)
