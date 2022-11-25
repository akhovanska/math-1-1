n = int(input())
lin = list(map(int, input().split()[:n]))
a = max(lin)
b = min(lin)
for i in range(0, n):
	if lin[i] == a:
		lin[i] = b
	elif lin[i] == b:
		lin[i] = a
	print(lin[i], end=' ')
