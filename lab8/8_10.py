from itertools import permutations

def permutation(list1):
   if len(list1) == 0:
       return []
   if len(list1) == 1:
       return [list1]
   l = []
   for i in range(len(list1)):
       m = list1[i]
       remlist1 = list1[:i] + list1[i+1:]
       for p in permutation(remlist1):
            l.append([m] + p)
   return l


perm_res = permutation(list1=[i for i in range(1, int(input()) + 1)])
for perm in perm_res:
    print(*perm)
