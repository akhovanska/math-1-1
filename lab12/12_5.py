def Fib(a):
    if(a == 1 or a == 2):
        return 1
    return Fib(a-1)+Fib(a-2)

x = int(input())
i=1
while True:
    if(x < Fib(i)):
        print(Fib(i-1))
        break
    i += 1
