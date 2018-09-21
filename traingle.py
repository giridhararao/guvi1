a=input()
if a.isdigit():
    a=int(a)
    b=a
    for i in range(0,a):
        c=[]
        for j in range(0,b):
            c.append("1")
        print(" ".join(str(x) for x in c))
        b=b-1
        print
else:
    print("Invalid")
