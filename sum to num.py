a,b=input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	z=[]
	y=0
	w=0
	c=input().split()
	for i in range(0,a):
		if c[i].isdigit():
			z.append(int(c[i]))
		else:
			w=w+1
	for i in range(0,len(z)):
		u=z[i]
		s=0
		for j in range(0,len(z)):
			if i==j:
				break
			else:
				s=u+z[j]
				if s==b:
					y=y+1
	if w>0:
		print("invalid")
	elif y>0:
		print("YES")
	elif y==0:
		print("NO")
else:
	print("Invalid")
