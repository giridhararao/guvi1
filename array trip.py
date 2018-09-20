a=input()
b=int(a)
c=input().split()
out=0
d=[]
e=0
for i in range(0,b):
    d.append(int(c[i]))
for i in range(1,b):
    e=d[i]-d[0]
    out=out+e
if(out>0):
    print(out)
else:
    print("0")
