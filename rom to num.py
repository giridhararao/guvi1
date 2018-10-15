n=input()
a=len(n)
o=0
b=a
if (n=='IX'):
	print("9")
elif (n=='XIX'):
	print("19")
elif(n=='XIV'):
        print("14")
elif(n=='IV'):
        print("4")
else:
	while(b>0):
		for i in range(0,a):
			if(n[i]=='I'):
				o=o+1
				b=b-1
			elif(n[i]=='X'):
				o=o+10
				b=b-1
			elif(n[i]=='V'):
				o=o+5
				b=b-1
	print(o)
