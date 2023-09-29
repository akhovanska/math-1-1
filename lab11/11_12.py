def S(n):
  if n==1:
    return 1
  elif n==2:
    return 1
  else:
    return S(n-2)+S(n-1)
x=int(input("Enter n:"))
for g in range(1, x+1):
  h=0
  k=0
  for f in range(2, S(g)):
    if S(g)%f==0:
      k=k+1
    else:
      pass
  for t in range(2, g):
    if g%t==0:
      h=h+1
    else:
      pass
  if k==0 and g==4:
    print(S(g), "просте,", "виконується")
  elif k==0 and h!=0:
    print(S(g), "просте,", "виконується")
  elif k!=0 and h!=0:
    print(S(g), "не просте,", "виконується")
  elif k==0 and h==0:
    print(S(g), "просте,", "виконується")
  else:
    print(S(g), "не просте,", "не виконується")
