x, y = input().split()
x = float(x)
y = float(y)
z = (2 * x * y) / (( x ** 2 + y ** 2) ** (1 / 2)) - (x + y - 1) ** 2 / (x * y)
print("%.3f" % z)