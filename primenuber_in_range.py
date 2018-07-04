a=int(input())
b=int(input())
i=0
for c in range(a, b+1):
   if c>1:
     for d in range(2,c):
        if((c%d)==0):
          break
        else:
          i=i+1
print(i)
