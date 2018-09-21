s=input().split()
a=0
for i in range(len(s)):
	g=s[i]
	if g[0].isupper() and g[1:].islower():
		a=a+1
if a==len(s):
	print ("yes")
else:
	print ("no")
