n, m=[int(d) for d in input().split( )]
mas=[]
for k in range(n):
	l=[int(d) for d in input().split( )]
	mas.append(l)
print(m, n)
for i in range(m):
	for h in range(n):
		if h==n-1:
			print(mas[0-(h+1)][i])
		else:
			print(mas[0-(h+1)][i], end=' ')
