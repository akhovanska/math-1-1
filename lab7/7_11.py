def d(a, y):
	f=''
	while a>0:
		g=a%y
		if g<10:
			f=str(g)+f
			a=a//y
		else:
			f=chr(87+g)+f
			a=a//y
	return 0 if f=='' else f
e=int(input())
h=0
v=[]
for vl in range(2,37):
	if d(e, vl)==d(e, vl)[::-1]:
		h+=1
		v.append(vl)
if h==0:
	print("none")
else:
	if h==1:
		print("unique")
		print(' '.join(map(str, v)))
	else:
		print("multiple")
		print(' '.join(map(str, v)))
