s=input()
b=s[::-1]
if s==b:
	print("0")
else:
	c=[]
	for i in range(0,len(s)):
		c.append(s[i])
	out=[]
	for i in c:
		if c.count(i)==1:
			out.append(i)
	print(len(out))
