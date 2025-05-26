n = int(input())
outcomes = input().strip()
_anton = 0
_danik = 0

for o in outcomes:
    if o == 'A':
        _anton += 1
    elif o == 'D':
        _danik += 1
if _anton == _danik:
    print("Friendship")
elif _anton > _danik:
    print("Anton")
else:
    print("Danik")