a=input()
b=[]
c=0
for i in range(0,len(a)):
    b.append(a[i])
for i in range(0,len(a)):
    c=c+ord(a[i])
print(c)
