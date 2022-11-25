s = input()
print(s[2] + s[6] + s[10])
print(s[0] + s[len(s)-2] + s[len(s)-1])
print(s[0 : 7])
print(s[4 : len(s)])
i = 1
sq = ''
while i < len(s):
	sq = sq + s[i]
	i += 2
print(sq)
print(len(sq))
print(s[::-1])
