n,d=raw_input().split()
if n.isdigit() and d.isdigit():
	n=int(n)
	d=int(d)
	l=[]
	a=0
	def rotate(l,d):
		return l[d:]+l[:d]
	c=raw_input().split()
	for i in range(0,n):
		if c[i].isdigit():
			l.append(c[i])
		else:
			a=a+1
	if a==0:
		g=rotate(l,d)
		for i in range(0,n):
			print int(g[i]),
	elif a>0:
		print "invalid"
else:
	print "Invalid"
