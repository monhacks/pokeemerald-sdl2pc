import sys

def swapendianess(filename):
    with open(filename, "rb") as e:
        contents = e.read()
        
    output = bytearray()
        
    for i in range(0,len(contents), 2):
        output += contents[i+1].to_bytes(1, 'little')
        output += contents[i].to_bytes(1, 'little')
        
    with open(filename, "wb") as e:
        e.write(output)
 

swapendianess(sys.argv[1])
print("swap done!")