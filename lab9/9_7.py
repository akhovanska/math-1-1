n = input()
s = input()

freq = {el: s.count(el) for el in set(s)}
for i in freq:
    if freq[i] % 2 == 1:
        print(i)
        break
else:
    print('Ok')
