n=raw_input()
n=int(n)
s=raw_input().split()
print int(s[0]),
for i in range(n-1):
	if int(s[i])<int(s[i+1]):
		print int(s[i]),
		s[i+1]=s[i]
	else:
		print int(s[i+1]),
