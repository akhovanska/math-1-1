#Добуток цифр трицифрового числа

n = abs(int(input()))
s = n//100
o = n%10
d = n//10
d2 = d%10
print(s*o*d2)
