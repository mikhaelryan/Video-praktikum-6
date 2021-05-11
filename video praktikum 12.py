kelas={'andi','rian','nanda','alvin','budi'}
print('1.presensi\n2.melihat daftar hadir\n3.melihat daftar tidak hadir\n4.exit')
inp=int(input('masukan pilihan: '))
hadir=set()
while inp!=4:
    if inp==1:
        n=str(input('nama mahasiswa: '))
        if n.lower() in kelas:
            hadir.add(n)
        else:
            print('bukan merupakan mahasiswa di kelas ini')
    elif inp==2:
        print('daftar mahasiswa yang hadir adalah ',hadir)
    elif inp==3:
        tidak_hadir=kelas.difference(hadir)
        print('daftar mahasiswa yang tidak hadir adalah ',tidak_hadir)
    inp=int(input('masukan pilihan: '))