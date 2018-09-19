n=int(input())
a=input().split()
b=input().split()
c=0
p=[]
q=[]
r=[]
for i in range(0,n):
    p.append(a[i])
    q.append(b[i])
for i in range(0,n):
        if(p==q):
            print(c)
            break
        else:
            r=p[1:n]
            r.append(a[0])
            p=r
            c=c+1
