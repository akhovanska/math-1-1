def d(x,y):
   l = ''
   while x>0:
       h=x%y
       if h<10:
           l=str(h)+l
           x=x//y
       else:
           l=chr(55+h)+l
           x=x//y
   return 0 if l == '' else l
f=int(input())
print(d(f,13))
