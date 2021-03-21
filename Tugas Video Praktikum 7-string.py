#input BAPAK makan
#proses
n=str(input('masukan kata :'))
x=len(n)
for i in range(x):
    if n[i].isupper():
        hasil1=n[i].lower()
        print(hasil1,end='')
    elif n[i].islower():
        hasil2=n[i].upper()
        print(hasil2,end='')
    else:
        print(n[i],end='')
#ouput bapak MAKAN