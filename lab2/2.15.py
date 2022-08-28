a, b, c = map(int, input().split())
D = b*b - 4*a*c
if D==0:
	x = (-b)/(2*a)
	print("One root:", int(x))
elif D>0:
	x1 =( -b + D**(1/2))/(2*a)
	x2 =( -b -  D**(1/2))/(2*a)
	if x1<x2:
		print("Two roots:", int(x1), int(x2))
	else:
		print("Two roots:", int(x2), int(x1))
else:
	print("No roots")
