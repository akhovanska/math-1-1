def S(n):
	if n == 0:
		return 1
	elif n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return 2*S(n-1)+3*S(n-3)
x = int(input("Enter a:"))
i = 1
while True:
	if S(i) <= x:
		i = i+1
	else:
		print(S(i - 1), i - 1)
		break
