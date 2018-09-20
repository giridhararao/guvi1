s=raw_input().split()
n=len(s)
for i in range(0,n):
	a=s[i]
	b=[]
	for i in range(1,len(a)):
		b.append(a[-i])
	b.append(a[0])
	print "".join(b),
