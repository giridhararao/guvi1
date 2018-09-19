n=input()
if n.isdigit():
	n=int(n)
	arr=input().split()
	for i in range(0,n):
		f=arr.count(arr[i])
		if f==1:
			print(arr[i])
		else:
			continue
else:
	print("invalid")
