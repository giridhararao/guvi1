a=int(input())
b=list();
i=0
for c in range(a):
  b=int(input())
for d in range(a):
  for e in range(a):
     if(b[d]!=b[e] and (d!=e)):
        i=i+1
   if(i==a)
     print(d)
