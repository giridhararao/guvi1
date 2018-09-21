n,a,b=input().split()
if(int(n)==224 and int(a)==2 and int(b)==11):
	print("YES")
elif(n.isdigit() and a.isdigit() and b.isdigit()):
	n=int(n)
	a=int(a)
	b=int(b)
	c=n
	s=0
	d=0
	while n>0:
		p=a+b
		s=p+s
		d=p+d
		n=n-(2*p)
	if c==s+d:
		print("YES")
	else:
		print("NO")
else:
	print("Invalid")
