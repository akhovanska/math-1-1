x=int(input())
n=int(input())
mas=[]
for k in range(n):
	l=[int(d) for d in input().split( )]
	mas.append(l)
for i in range(n):
	p=False
	for j in range(n):
		if mas[j][i]==x:
			p=True
			break
		else:
			pass
	if p:
		print("YES")
	else:
		print("NO")
