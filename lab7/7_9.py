def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse(n):
    n = str(n)
    return int(n[::-1])
K = int(input())
i = 0
j = 0
while True:
    if isPrime(i) and isPrime(reverse(i)) and i != reverse(i):
        j += 1
        if j == K:
            print(i)
            break
    i += 1
