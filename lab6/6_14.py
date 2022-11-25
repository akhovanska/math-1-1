s = input()
k = s.replace(' ', '')
n = 0
for i in range(0, len(k)):
	if k[i] != k[len(k) - 1 - i]:
		break
	else:
		n += 1
if n == len(k):
	print('YES')
else:
	print('NO')
