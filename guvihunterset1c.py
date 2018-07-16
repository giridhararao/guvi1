n=int(raw_input())
b=raw_input().split()
d=len(b)
s=[]
count=0
for i in range(0,d):
	if(int(b[i])==i):
		count=count+1
		f=b[i]
		s.append(f)
e=len(s)
p=[]
if count>0:
	for j in range(0,e):
		largest=int(s[0])
		g=len(s)
		for i in range(1,g):
			if(largest>int(s[i])):
				largest=int(s[i])
		p.append(largest)
		s.remove(str(largest))
	t=len(p)
	for y in range(0,t):
		print p[y],
else:
	print "-1"
