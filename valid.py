te=input()
if '@' in te:
	if te.count('@') and te.count('.') ==1:
		t=te.index('@')
		s=te.index('.')
		if len(te[t+1:s])==5:
			if len(te[:t])>=3:
				if '.com' in te:
					print("YES")
				else:
					print("NO")
			else:
				print ("NO")
		else:
			print("NO")
	else:
		print("NO")
else:
	print("NO")
