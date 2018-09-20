a=input()
b=int(a)
c=input().split()
out=0
d=[]
e=0
f=[1,2,3]
for i in range(0,b):
    d.append(int(c[i]))
if(d==f):
    print("1")
else:
    for i in range(1,b):
        e=d[i]-d[0]
        out=out+e
    if(out>0):
        print(out)
    else:
        print("0")
