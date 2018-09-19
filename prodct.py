a=raw_input()
while True:
	try:
		if a.isdigit():
			a=int(a)
			if a<=1000:
				b=raw_input().split()
				z=[]
				for i in range(0,a):
					s=1
					for j in range(0,a):
						if j==i:
							t=1
						else:
							s=s*int(b[j])
					print s,
			else:
				print("Input is out of range")
		else:
			print("invalid")
			break
	except:
		break
