a,b=input().split()
z=len(a)
y=len(b)
u=a
v=b
e=[]
f=[]
g=[]
for i in range(0,z):
	if(i==0):
		s=a[i].upper()
		e.append(s)
	elif(i>0):
                s=a[i].lower()
                e.append(s)
n="".join(e)
g.append(n)
for i in range(0,y):
	if(i==0):
		s=b[i].upper()
		f.append(s)
	elif(i>0):
                s=b[i].lower()
                f.append(s)
m="".join(f)
g.append(m)
print(" ".join(str(x) for x in g))
