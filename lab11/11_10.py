def F1(n):
  if(n < 5):
    return 1
  return F1(n-1)+F1(n-5)
def F2(n):
  if(n < 8):
    return 1
  return F2(n-2)+F2(n-4)+F2(n-8)
def F3(n):
  if(n < 7):
    return 1
  return 2*F3(n-2)-F3(n-7)
def F4(n):
  if(n < 14):
    return 1
  return 4*F4(n-5)+F4(n-14)

N = int(input())
print("a: ", F1(N))
print("b: ", F2(N))
print("c: ", F3(N))
print("d: ", F4(N))
