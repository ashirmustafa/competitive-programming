_str = input()

_list = []

for char in _str:
    try:
        int(char)
        _list.append(char)
    except ValueError:
        pass
    
_list.sort()

print("+".join(_list))
