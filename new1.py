n=int(input())
a=input().split()
b,c=input().split()
z=0
for i in range(n):
        if(b==a[i]):
          start=b
          last=c
        elif(c==a[i]):
          start=c
          last=b
for i in range(0,n):
      if(a[i]==start):
            x=i
            break
for i in range(0,n):
     if(a[i]==last):
          y=i
          break
if(x>y):
    print(x-y)
else:
    print(y-x)
