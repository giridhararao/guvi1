n=input()
if n.isdigit():
	n=int(n)
	l=[]
	w=0
	for i in range(0,n):
		b=input().split()
		c=len(b)
		for j in range(0,n):
			if b[j].isdigit():
				l.append(int(b[j]))
			else:
				w=w+1
	if w==0:
		x=0.000000
		y=0.000000
		for i in range(0,len(l)):
			x=x+l[i]
			y=y+1
		a=x/y
		print("%.6f"%a)
	else:
		print("Invalid")
else:
	print("Invalid")
