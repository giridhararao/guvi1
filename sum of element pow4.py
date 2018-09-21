a=input()
b=[]
x=len(a)
c=0
for i in range(0,len(a)):
    b.append(int(a[i]))
for i in range(0,len(a)):
    c=c+(b[i]**x)
print(c)
