n=input()
c=[]
if n.isdigit():
		a=1
		b=int(n)
		for num in range(a+1,b):
			if num>1:
				for i in range(2,num):
					if(num%i==0):
						break
				else:
					c.append(num)
		print(" ".join(str(x) for x in c))
