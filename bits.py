n=input()
a=int(n)
b=2**a
for i in range(0,b):
    print("".join(str(1 & int(i) >> x) for x in range(a)[::-1]))
