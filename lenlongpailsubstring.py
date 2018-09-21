s=input()
l=[]
m=[]
for i in range(0,len(s)):
	for j in range(i,len(s)):
		z=s[i:j+1]
		y=z[::-1]
		if z==y:
			l.append(z)
			m.append(len(z))
y=max(m)
for i in range(0,len(s)):
	if m[i]==y:
		ref=len(l[i])
		break
print(ref)
