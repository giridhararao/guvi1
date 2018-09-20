l,r,n=input().split()
if l.isdigit() and r.isdigit() and n.isdigit():
	l=int(l)
	r=int(r)
	out=0
	for j in range(l,r):
		if n in str(j):
			out=out+1
	print(out)
