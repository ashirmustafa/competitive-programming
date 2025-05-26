n = input()
tlc = 0
tuc = 0

for char in n:
    if char == char.upper():
        tuc = tuc + 1
    elif char == char.lower():
        tlc = tlc + 1



if tlc >= tuc:
    n = n.lower()
    print(n)
else:
    n = n.upper()
    print(n)
    