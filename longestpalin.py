s=input()
l=[]
m=[]
ref=0
for i in range(0,len(s)):
        for j in range(i,len(s)):
                z=s[i:j+1]
                y=z[::-1]
                if z==y:
                      l.append(z)
                      m.append(len(z))
x=max(m)
for i in range(0,len(s)):
        if(m[i]==x):
                ref=i
                break
print(l[i])
