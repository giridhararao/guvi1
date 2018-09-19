n=int(raw_input())
arr=raw_input().split()
min=9999
for i in range(0,n):
	w=int(arr[i])
	for j in range(0,n):
		if i==j:
			continue
		else:
			y=w+int(arr[j])
			y=abs(y)
			if min>y:
				min=y
				a=w
				b=arr[j]
if a>0:
	print a,
	print b
else:
	print b,
	print a
