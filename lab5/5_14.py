n, k = map(int, input().split())
lin = list(map(int, input().split()[:n]))
lin.sort()
print(lin[k-1])
