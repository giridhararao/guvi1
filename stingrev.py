a=input().split()
b=[]
for i in range(0,2):
    b.append(a[i])
b=b[::-1]
print(" ".join(str(x) for x in b))
