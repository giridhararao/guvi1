a=int(input())
i=0
j=0
c=list();
while a>0 :
  c[i]=a%10
  a=a//10
  i=i+1
for b in range(i)
  j=j+(c[b]*c[b])
print(j)
