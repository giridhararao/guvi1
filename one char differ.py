a,b=input().split()
c=len(a)
d=len(b)
out=0
if(c==d):
        for i in range(0,c):
                z=a[i]
                y=b[i]
                if(z==y):
                        out=0
                else:
                        out=out+1
        if(out==1):
                print("yes")
        else:
                print("no")
else:
        print("no")
