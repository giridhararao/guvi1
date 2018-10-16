a,b=input().split()
c=input().split()
a=int(a)
b=int(b)
d=[]
for i in range(0,a):
  d.append(c[i])
for i in range(0,b):
  x=d[i]
  d[i]=d[i+1]
  d[i+1]=x
print(" ".join(str(y) for y in d))
