#Сума цифр двоцифрового числа

x = abs(int(input()))
first = x // 10 # first - перша цифра числа
second = x % 10 # second - друга цифра числа
suma = first + second
print(suma)
