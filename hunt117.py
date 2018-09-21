a=input()
b=[]
out=0
for i in range(0,len(a)):
    b.append(int(a[i]))
for i in range(0,len(a)):
    out=out+(b[i]**i)
print(out)
