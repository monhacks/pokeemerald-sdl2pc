import sys
listlz = []
listun = []
listfinal = []

def swapendianess(filename):
    with open(filename, "rb") as e:
        contents = e.read()
        
    output = bytearray()
        
    for i in range(0,len(contents), 4):
        output += contents[i+3].to_bytes(1, 'little')
        output += contents[i+2].to_bytes(1, 'little')
        output += contents[i+1].to_bytes(1, 'little')
        output += contents[i].to_bytes(1, 'little')
        
    with open(filename, "wb") as e:
        e.write(output)
 

from pathlib import Path

#swapendianess(path)

allbins = Path('.').rglob('*.4bpp')

for path in allbins:
    print(path)
    swapendianess(path)
        
