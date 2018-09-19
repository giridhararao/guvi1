n=input().split('#')
m=input().split('#')
s=0
s1=0
for i in range(1,len(n)):
	s=s+int(n[i])
	s1=s1+int(m[i])
if s>s1:
	print(n[0])
else:
	print(m[0])
