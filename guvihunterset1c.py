a=int(input())
b=list();
c=list();
i=0
for c in range(a):
  b[c]=int(input())
for d in range(a):
   if(b[d]==d):
     c[i]=d
     i=i+1
if(i!=0):
  c.sort()
  print(c)
else:
  print("-1")
