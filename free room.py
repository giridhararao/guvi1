n,k=input().split()
n=int(n)
k=int(k)
c=0
a=input().split()
for i in range(n):
	if int(a[i])<=k:
		c=c+1
print(c)
