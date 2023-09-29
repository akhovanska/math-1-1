def a(b):
	c = ' '
	while b>0:
		c=str(b%2)+c
		b=b//2
	return c
d=int(input())
f=[]
for t in a(d):
	if t=="0":
		f.append("S")
	else:
		f.append("SX")
del f[-1]
del f[0]
u=0
while u<len(f):
	print(f[u], end='')
	u+=1
