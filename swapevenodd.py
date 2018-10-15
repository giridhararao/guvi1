s=input()
l=len(s)
a=[]
for i in range(0,l):
	a.append('0')
for i in range(0,l):
	if(i%2==0):
		a[i]=s[i+1]

	else:
		a[i]=s[i-1]

k="".join(a)
print(k)
