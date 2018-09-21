a=input()
b=[]
s=0
d=0
for i in range(0,len(a)):
    d=a.count(a[i])
    if(d==1):
        b.append(a[i])
print("".join(str(x) for x in b))
