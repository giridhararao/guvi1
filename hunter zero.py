a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
s=0
p=[]
ori=[]
ui=[]
for i in range(0,a):
    a=raw_input().split()
    l.append(a)
for i in range(0,len(l)):
    k=l[i]
    t=l[i]
    for j in range(0,len(k)):
        if '0' in k:
            u=[index for index, ink in enumerate(k) if ink=='0']
            for et in range(0,len(u)):
                ui.append(u[et])
            k=[]
            for r in range(0,len(l[i])):
                k.append('0')
            ori.append(k)
            k=[]
            break
        else:
            s=s+1
    if s==b:
        for z in range(0,b):
            p.append(t[z])
        ori.append(p)
        p=[]
    s=0
for i in ori:
  out=i
  for j in range(0,len(out)):
    if j in ui:
      out.insert(j+1,'0')
      out.remove(out[j])
  for i in range(0,len(out)):
    print out[i],
  print "\n",
