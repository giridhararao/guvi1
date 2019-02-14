import sys,string
n1,n2 = input().split()
n1,n2 = int(n1),int(n2)
if n2 > (2+2*n1) :
    print(-1)
    sys.exit()
if n1 > n2-1 :
    print(-1)
    sys.exit()
s = ''
if n2-n1 == 1 :
    s = '1'+'01'*n1
    print(s)
    sys.exit()
while n2 > n1 and n1 > 0:
    if n2-n1 == 1 :
        break
    n2 -= 2
    n1 -= 1
    #print(n2,n1)
    s += '110'
if n2-n1 == 1 :
    s += '10'*n1+'1'
    print(s)
    sys.exit()
if n2 > 2 and n1==0 :
    print(-1)
    sys.exit()
elif n1==1 and n2==1 :
    s += '0'+'1'*n2
elif n1==1 and n2==2 :
    s += '101'
elif n1==0:
    s += '1'*n2
print(s)
