a=input()
z=[]
out1=0
out2=0
if a.isdigit():
	a=int(a)
	b=input().split()
	min=int(b[0])
	for i in range(a):
		if min>int(b[i]):
			min=int(b[i])
	f=min
	max=int(b[0])
	for i in range(a):
		if max<int(b[i]):
			max=int(b[i])
	g=max
	for i in range(a):
		if(int(b[i])==int(f)):
			l=i
		elif(int(b[i])==int(g)):
			t=i

out1=l+1
out2=t+1
z.append(out1)
z.append(out2)
print(" ".join(str(x) for x in z))
