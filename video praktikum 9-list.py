inp=str(input('masukan kata: '))
x=inp.split(',')
y=len(x)
for i in range(y):
    m=x[i].split()
    n=len(m)
    v=str(x[0:i])
    if m[n-1] in v:
        continue
    tab=[]
    for j in range(y):
        g=x[j].split()
        h=len(g)
        if m[n-1] in g[h-1]:
            tab.append(x[j])
    print(tab)