alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
str = input()
k = int(input())
sh =''
n = 0
for i in range(0, len(str)):
	n = 0
	while str[i] != alf[n]:
		n += 1
	sh = sh + alf[n - k]
print(sh)
