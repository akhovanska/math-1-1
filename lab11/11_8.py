def fa(x):
    if(x == 1):
        return 1
    return x * fa(x-1)

def F1(n):
    P = 1
    for i in range(2 , n+1):
        P *= (1 - 1/(i**2))
    return P

def F2(n):
    P = 1
    for i in range(1 , n+1):
        P *= (2 + 1/(fa(i)))
    return P

def F3(n):
    P = 1
    for i in range(1 , n+1):
        P *= (i+1)/(i+2)
    return P

N = int(input())
print("a: ", F1(N))
print("b: ", F2(N))
print("c: ", F3(N))
