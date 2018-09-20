s=input()
a=[]
for i in s:
      if i not in a:
            a.append(i)
a.sort(reverse=True)
print("".join(str(x) for x in a))
