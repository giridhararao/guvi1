a=input()
b=[]
c=0
for i in range(0,len(a)):
    b.append(int(a[i]))
for i in range(1,len(a)+1):
    for j in range(0,i):
        c=c+b[j]
print(c)
