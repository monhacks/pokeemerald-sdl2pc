from pathlib import Path

allbins = Path('.').rglob('*.bin')

counter = 0

for path in allbins:
    print(path)
    counter += 1
    
print(counter)