n=int(input())
mas=[]
for k in range(n):
	l=[int(d) for d in input().split( )]
	mas.append(l)
sumg=0
sumd=0
for i in range(n):
	sumg+=mas[i][i]
	sumd+=mas[i][n-i-1]
print(sumg, sumd)
