n=input()
if n.isdigit():
	n=int(n)
	k=0
	for i in range(0,n):
		if 2**i==n:
			print("YES")
			break
		else:
			k=k+1
if k==n:
	print ("NO")
