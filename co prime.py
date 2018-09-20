n,m=input().split()
if n.isdigit() and m.isdigit():
	n=int(n)
	m=int(m)
	a=[n,m]
	x=0
	for i in range(0,2):
		num=a[i]
		s=0
		for j in range(2,num):
			if num%j==0:
				continue
			else:
				s=s+1
		if s==num-2:
			x=x+1
	if x==2:
		print("yes")
	else:
		print("no")
