n=input()
a=[]
out=0
for i in range(0,len(n)):
    a.append(int(n[i]))
for i in range(0,len(n)):
    if(i==(len(n)-1)):
        out=out+(a[i]*a[0])
    else:
        out=out+(a[i]**(i+2))
print(out)
