def isNearlyLucky(_str) -> str:
    _len = len(_str)
    count = 0
    for s in _str:
        if s == '4' or s == '7':
            count += 1
    if (count == 4) or (count == 7):
        return "YES"
    else:
        return "NO"

n = input()
print(isNearlyLucky(n))
    
    