#Формула Герона

a, b, c, d, f = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
f = float(f)
p = (a + b + f) / 2
s = (p * (p - a) * (p - b) * (p - f)) ** (1 / 2)
k = (c + d + f) / 2
m = (k * (k - c) * (k - d) * (k - f)) ** (1 / 2)
q = s + m
print(" %.4f " % q)
