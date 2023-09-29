n = int(input())
m = [int(el) for el in input().split()]
L = []
m_s = set(m)
for i in m_s:
     if abs(i) not in L:
         L.append(i)
print(len(L))
