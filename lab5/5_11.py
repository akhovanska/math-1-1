n = int(input())
lin = list(map(int, input().split()[:n]))
print(lin[n-1], end=' ')
for i in range(0, n - 1):
	print(lin[i], end=' ')
