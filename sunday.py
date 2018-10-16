a=input().split()
b=len(a)
for i in range(0,b):
  if(a[i]=='Sunday'):
    print("yes")
  elif(a[i]=='Saturday'):
    print("yes")
  else:
    print("no")
