a=int(input())
b=[]
c=[]
d=[]
for i in range(a):
  x=int(input())
  b.insert(i,x)
for j in range(a):
  x=int(input())
  c.insert(j,x)
d=b[::-1]
if(b==d):
   print("Yes")
else:
   print("No)
