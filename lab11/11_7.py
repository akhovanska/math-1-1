def F(n, i):
    if(i == n):
        return 2 + 1/(4*n+2)
    return 2 + 1/(4*i + F(n, i+1))

N = int(input())
print(F(N, 1))
