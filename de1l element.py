a,b=input().split()
c=input().split()
a=int(a)
b=int(b)
d=[]
g=[]
z=0
for i in range(0,a):
    e=int(c[i])
    d.append(e)
for i in range(0,a):
    f=int(d[i])
    if(b!=f):
        g.append(f)
        z=1
if(z==0):
    print('empty')
else:
    print(" ".join(str(x) for x in g))
