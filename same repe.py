n=input()
if n.isdigit():
	n=int(n)
	b=input().split()
	c=input()
	o=0
	for i in range(n):
		if c in b[i]:
			o=o+1
	print(o)
