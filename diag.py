a=input()
if a.isdigit():
	a=int(a)
	l=[]
	s=0
	for i in range(0,a):
		b=input().split()
		l.append(b)
	for i in range(0,a):
		h=l[i]
		for j in range(0,len(h)):
			if i==j:
				s=s+int(h[j])
	print(s)
