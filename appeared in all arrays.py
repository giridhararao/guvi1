a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
o=[]
h=[]
for i in range(0,a):
	w=raw_input().split()
	l.append(w)
for i in range(0,len(l)-1):
  k=l[i]
  z=l[i+1]
  for j in range(0,b):
    if k[j] in z:
        o.append(k[j])
for i in range(0,len(o)):
    t=o.count(o[i])
    if t==a-1:
        h.append(o[i])
h=list(set(h))
h.sort()
for i in range(0,len(h)):
    print h[i],
