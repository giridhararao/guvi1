n=input()
a=int(n)
b=input().split()
c=[]
d=[]
for i in range(0,a):
    c.append(int(b[i]))
for i in range(0,a):
    if(i==(a-1)):
        x=-1
        d.append(x)
    elif(c[i]>c[i+1]):
        d.append(c[i+1])
    else:
        y=-1
        d.append(y)
print(" ".join(str(z) for z in d))
