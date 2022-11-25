def a(x, y):
	i=0
	for b in range(len(x)):
		for c in range(y):
			if c<10:
				if x[b]==str(c):
					i=c*y**(len(x)-b-1)+i
					break
			else:
				if x[b]==chr(55+c):
					i=c*y**(len(x)-b-1)+i
	return i
def d(a, y):
	f=' '
	while a>0:
		g=a%y
		if g<10:
			f=str(g)+f
			a=a//y
		else:
			f=chr(55+g)+f
			a=a//y
	return 0 if f==' ' else f
e, h= [int(gh) for gh in input().split( )]
v= input()
if h==10:
	print(a(v, e))
elif e==10:
	print(d(int(v), h))
else:
	print(d(a(v, e), h))
