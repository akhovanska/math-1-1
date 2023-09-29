def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

def Fa(x, e):
    if e == 0:
        return 0
    return (x**(2*e+1))/factorial(e)+Fa(x, e-1)

def Fb(x, e):
    if e == 0:
        return 0
    return -((-x)**e)/e + Fb(x, e-1)

def Fc(x, e):
    if e == 0:
        return 1
    return -((-x)**e) + Fc(x, e-1)

def Fd(x, e):
    if e == 1:
        return 1
    return (((-1)**(e+1))*e*(e+1)*x/2)+Fd(x, e-1)

X = int(input())
E = int(input())
print(Fa(X, E))
print(Fb(X, E))
print(Fc(X, E))
print(Fd(X, E))
