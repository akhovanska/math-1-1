s = input()
k = 'k'
k = k*(-1)
for n in range(0, len(s)):
	if s[n] == ' ' or s[n] == '.' or s[n] == ',' or s[n] == '?' or s[n] == '!' or s[n] == ':' or s[n] == '-' or s[n] == '—':
		k = k + s[n]
	else:
		k = k + s[n] + s[n]
print(k)
