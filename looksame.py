a,b=input().split()
al=len(a)
bl=len(b)
c=[]
d=[]
if al==bl:
	for i in range(0,al):
		c.append(a[i])
	x=len(list(set(c)))
	for j in range(0,bl):
		d.append(b[j])
	y=len(list(set(d)))
if(x==y):
	print("yes")
else:
	print("no")
