n=raw_input()
if n.isdigit():
	n=int(n)
	a=1
	for i in range(0,n):
		for j in range(0,a):
			print "1",
		a=a+1
		print 
else:
	print "Invalid"
