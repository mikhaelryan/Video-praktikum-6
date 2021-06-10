inp=str(input('masukan: ')
inp=inp.split()
import re
for i in inp:
    if re.search('((^http://|https://)?)[a-zA-Z0-9]+[.]+[a-zA-Z0-9]+',i):
        print(i)
