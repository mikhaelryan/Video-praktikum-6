#input jumlah baris setengah belah ketupat
n=int(input('masukan angka: '))
#proses
for i in range(1,(2*n)+1):
    if i<=n:
        x=n-i
        for j in range(1,x+1):
            print(' ',end='')
        print(i*'* ')#ouput
    elif i>n:
        x=x+1
        for j in range(1,x+1):
            print(' ',end='')
            y=x+j
        print((i-y)*'* ')#output