from math import sqrt
from random import randint

#getting input through list
def cash(fun):
    results = {}

    def _cash(*args):
        if args not in results:
            results[args] = fun(*args)
        return results[args]

    return _cash

#recursive method of getting fibbonachi number
@cash
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#checking if it is a prime number through iterating
@cash
def is_prime(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
        return True

#iterating with all decorators
def density(a):
    m = a * 1000
    passed = 0
    for _ in range(m):
        k = randint(1, a)
        if is_prime(k):
            passed += 1
    return passed / m

#checking the decorator
#a = 50
#print("[1, {}]:{:.0f}%".format(a, 100 * density(a)))
