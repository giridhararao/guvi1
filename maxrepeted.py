n=int(input())
a=input().split()
def repeated():
	k=0
	for i in range(0,n):
		s=a.count(a[i])
		if s>1:
			print(a[i])
			break
		else:
			k=k+1
	if k==n:
		print("unique")

if n==len(a):
	repeated()
elif n>len(a):
	n=len(a)
	repeated()
else:
	j=len(a)-n
	for i in range(1,j+1):
		a.remove(a[-i])
	repeated()
