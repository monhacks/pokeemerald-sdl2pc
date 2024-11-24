import sys
listlz = []
listun = []
listfinal = []

def swapendianess(filename):
    with open(filename, "rb") as e:
        contents = e.read()
        
    output = bytearray()
        
    for i in range(0,len(contents), 2):
        output += contents[i+1].to_bytes(1, 'little')
        output += contents[i].to_bytes(1, 'little')
        
    with open(filename, "wb") as e:
        e.write(output)
 

from pathlib import Path

#swapendianess(path)

allbins = Path('.').rglob('*.gbapal.lz')

for path in allbins:
    listlz.append('.'.join(str(path).split('.')[0:2]))

allbins = Path('.').rglob('*.gbapal')

for path in allbins:
    listun.append(path)
    if str(path) in listlz:
        print(path)
        swapendianess(path)
        
