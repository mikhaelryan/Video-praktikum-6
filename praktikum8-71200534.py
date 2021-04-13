y=input('nama file: ')
x=open(y,'r')
n=str(input('kata yand dicari: '))
for line in x:
    a=line.split()
    p=len(a)
    for i in range(p):
        if a[i].lower()==n.lower():
            b='\033[1;30;42m'+a[i]+'\033[0m'
            print(b,end=' ')
        else:
            print(a[i],end=' ')
    print()