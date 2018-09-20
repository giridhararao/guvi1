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
                    w= set()
                    longest = y
                    w.add(S[i-y+1:i+1])
                elif y == longest:
                    w.add(S[i-y+1:i+1])

    return w
a=input()
b=input()
ret = lcs(a,b)
for x in ret:
    print(x)
