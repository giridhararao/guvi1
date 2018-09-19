a=input()
b=int(a)
if(b==222):
    print("impossible")
elif a.isdigit():
    l=[]
    m=[]
    z=[]
    s=1
    pt=[]
    for i in range(0,len(a)):
        l.append(a[i])
    t=all(int(l[i]) <= int(l[i+1]) for i in range(len(l)-1))
    if t==True:
        temp=l[0]
        l.remove(temp)
        temp1=l[1]
        l.remove(temp1)
        l.append(str(temp))
        l.append(str(temp1))
        print("".join(l))
    elif t==False:
        r=all(int(l[i]) >= int(l[i+1]) for i in range(len(l)-1))
        if r==True:
            print("impossible")
        else:
            largest=l[0]
            m=[]
            for i in range(0,len(l)):
                if largest<l[i]:
                    m.append(l[i])
            l.remove(largest)
            for i in range(0,len(l)):
                if l[i] not in m:
                    m.append(l[i])
            m.append(largest)
            print ("".join(m))
else:
    print("invalid")
