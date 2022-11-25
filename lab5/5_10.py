n = int(input())
lin = list(map(int, input().split()[:n]))
m = int(input())
lim = list(map(int, input().split()[:m]))
n, i = 0, 0
lix= []
while n != len(lin):
	chk = True
	for m in range(0, len(lim)):
		if lin[n] == lim[m]:
			chk = False
			break
	if chk:
		lix.append(lin[n])
	n += 1
print(len(lix))
while i != len(lix):
	print(lix[i], end=' ')
	i += 1
