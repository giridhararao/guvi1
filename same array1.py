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
                    w=[]
                    longest = y
                    w.append(S[i-y+1:i+1])
                elif y == longest:
                    w.append(S[i-y+1:i+1])
    w=w[::-1]

    print(w[0])
a=input()
b=input()
lcs(a,b)
