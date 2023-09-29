n, m=[int(d) for d in input().split( )]
mas=[]
maspr=[]
for k in range(n):
	l=[int(d) for d in input().split( )]
	mas.append(l)
input()
for f in range(n):
	h=[int(d) for d in input().split( )]
	maspr.append(h)
sumh=0
for j in range(n):
	for i in range(m):
		sumh+=(mas[j][i])*(maspr[j][i])
print(sumh)
