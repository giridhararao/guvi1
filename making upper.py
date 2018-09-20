s=input().split()
k=[]
for i in range(0,len(s)):
	g=len(s[i])
	k.append(g)
b="".join(s)
l=[]
for i in range(0,len(b)):
	if i%2==0:
		d=b[i].upper()
		l.append(d)
	else:
		l.append(b[i])
out=[]
h="".join(l)
m=0
for i in range(0,len(k)):
	out.append(h[m:k[i]+m])
	m=k[i]+m
print(" ".join(str(x) for x in out))
