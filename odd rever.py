n=input().split()
a=[]
for i in range(0,len(n)):
        if(i%2==0):
            b=n[i][::-1]
            a.append(b)
        else:
            a.append(n[i])
print(" ".join(str(x) for x in a)) 
