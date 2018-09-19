n=int(input())
a=input().split()
b=input().split()
p=[]
q=[]
r=[]
c=0
for i in range(0,n):
    p.append(a[i])
    q.append(b[i])
for i in range(0,n):
    if(p==q):
        print(c)
        break
    else:
        r=p[1:n]
        r.append(p[0])
        p=r
        c=c+1
