a,b=input().split()
c=[]
d=[]
cost=0
for i in range(0,len(a)):
    c.append(a[i])
for i in range(0,len(b)):
    d.append(b[i])
for i,j in zip(range(0,len(a)), range(0,len(b))):
        if (c[i]!=d[i]):
            if(d[i]>c[i]):
                cost=cost+(ord(d[i])-ord(c[i]))
            else:
                cost=cost+(ord(c[i])-ord(d[i]))
        elif(c[i]==d[i]):
            continue
print(cost)
