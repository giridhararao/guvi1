def sample(n):
    c=0
    while(n):
      c+=n&1
      n>>1
    return c
a=int(input())
b=list();
d=list();
for i in range(a):
   b[i]=int(input())
for j in range(a): 
   d[j]=sample(b[j])
d.sort(reverse=true)
print(d)
 

  
