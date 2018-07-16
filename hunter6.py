a=int(input())
b=input().split()
def repeated():
	k=0
	for i in range(0,a):
		s=b.count(b[i])
		if s>1:
			print(b[i])
			break
		else:
			k=k+1
	if k==a:
		print("unique")

if a==len(b):
	repeated()
elif a>len(b):
	a=len(b)
	repeated()
else:
	j=len(b)-a
	for i in range(1,j+1):
		b.remove(b[-i])
	repeated()
