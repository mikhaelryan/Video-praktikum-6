inp=str(input('masukan data?(Y/T): '))
x=[]
y=[]
z=[]

while inp.lower()=='y':
    n=(input('masukan data(nama,nim,prodi): '))
    n=n.split(',')
    n=tuple(n)
    nama,nim,prodi=n
    x.append(nama)
    y.append(nim)
    z.append(prodi)
    dic={'Nama: ':x,'NIM: ':y,'Prodi: ':z}
    inp=str(input('masukan data?(Y/T): '))
print(dic)

