def fa(x):
    if(x == 0):
        return 1
    return x * fa(x-1)

def F1(a , i):
    a = (a**(2*i+1))/fa(2*i+1)
    return a
def F2(a, i):
    a = ((-1)**i)*(a**i)/i
    return a
def F3(a, i):
    a = ((-1)**i)*(a**i)/fa(i*i+i)
    return a
def F4(a, i):
    a = (i+1)*((a**i)/fa(i))
    return a

x = int(input())
k = int(input())
if(k >= 0):
    print("a: ", F1(x, k))
    print("c: ", F3(x, k))
    print("d: ", F4(x, k))
if(k >= 1):
    print("b: ", F2(x, k))
