def lcs(S,T):
    n = len(S)
    m = len(T)
    counter = [[0]*(m+1) for x in range(n+1)]
    longest = 0
    w= set()
    for i in range(n):
        for j in range(m):
            if S[i] == T[j]:
                y = counter[i][j] + 1
                counter[i+1][j+1] = y
                if y > longest:
                    out=[]
                    longest = y
                    out.append(S[i-y+1:i+1])
                elif y == longest:
                    out.append(S[i-y+1:i+1])
    out=out[::-1]

    return(out[0])
x,y=input().split()
a=len(x)
b=len(y)
big=0
if(a>b):
    big=a
else:
    big=b
c=[]
c=lcs(x,y)
d=len(c)
if(d==1):
    print(big)
else:
    print(big-d)
