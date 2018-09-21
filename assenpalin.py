a=input()
l=[]
ref=[]
for i in range(0,len(a)):
	for j in range(0,len(a)):
		z=a[i:j+1]
		y=z[::-1]
		if z==y:
			l.append(z)
for i in l:
	if len(i)>1:
		ref.append(i)
ref.sort(key=len)
for out in ref:
	print(out)
