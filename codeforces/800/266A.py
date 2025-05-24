_i_n = int(input())
_i_str = input()
moves = 0
for i in range(1, _i_n):
    if(_i_str[i] == _i_str[i - 1]):
        moves += 1
        
print(moves)