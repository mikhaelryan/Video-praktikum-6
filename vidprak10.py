print('pilihan:\n1.menambahkan username dan email\n2.mencari email\n3.exit')
inp=int(input('masukan pilihan: '))
d={}
while inp!=3:
    if inp==1:
        user=str(input('masukan username: '))
        email=str(input('masukan email: '))
        x=email.split('@')
        if x[1]=='ukdw.ac.id':
            d.update({user:email})
    elif inp==2:
        cari=str(input('cari email dari: '))
        x=d.get(cari)
        print('email dari ',cari,' adalah ',x)
    inp=int(input('masukan pilihan: '))
print(d)