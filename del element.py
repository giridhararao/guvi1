a,b=input().split()
c=input().split()
a=int(a)
b=int(b)
d=[]
g=[]
for i in range(0,a):
    e=int(c[i])
    d.append(e)
for i in range(0,a):
    f=int(d[i])
    if(b!=f):
        g.append(f)
print(" ".join(str(x) for x in g))
