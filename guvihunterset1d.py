a=int(input())
b=input().split()
c=len(b)
for i in range(0,c):
	z=b.count(b[i])
	if (z<2):
		print(b[i])
