n=int(input())
mas=[]
for k in range(n):
	l=[int(d) for d in input().split( )]
	mas.append(l)
r, c=[int(f)for f in input().split( )]
for i in range(r):
	for h in range(c):
		if h==c-1:
			print(mas[i][h])
		else:
			print(mas[i][h], end=' ')
