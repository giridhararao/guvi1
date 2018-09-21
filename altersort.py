a=input()
b=input().split()
c=[]
d=[]
e=[]
z=0
for i in range(0,len(b)):
    c.append(int(b[i]))
c.sort()
l=(len(c)-1)
for i in range(0,len(c)):
    if(i%2==0):
        d.append(c[l])
        l=l-1
    else:
        d.append(c[z])
        z=z+1
print(" ".join(str(x) for x in d))
