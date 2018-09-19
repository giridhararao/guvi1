a=input()
b=len(a)
c=[]
for i in range(0,b):
    c.append(a[i])
t=len(list(set(c)))
if((b%t)==1):
    print("YES")
else:
    print("NO")
