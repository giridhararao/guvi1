n=input()
s=int(n)
a=input().split()
out=0
e=0
b=[]
c=[1,2,3]
for i in range(0,s):
    b.append(int(a[i]))
if(b==c):
  print("1")
else:
  for i in range(1,s):
      e=b[i]-b[0]
      out=out+e
  if(out>0):
      print(out)
  else:
      print("0")
