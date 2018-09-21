n=input()
c=[]
out=0
if n.isdigit():
    a=1
    b=int(n)
    for num in range(a+1,b):
        if num>1:
            for i in range(2,num):
                if(num%i==0):
                    break
                else:
                    c.append(num)
    for i in range(0,len(c)):
        x=int(c[i])
        if(x%10==3):
            out=out+x
    print(out)
