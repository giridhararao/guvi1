n=int(raw_input())
b=raw_input().split()
c=len(b)
for i in range(0,c):
	if i%2==0:
		b[i]=int(b[i])
		if b[i]%2!=0:
			print b[i],
	else:
		b[i]=int(b[i])
		if b[i]%2==0:
			print b[i],
