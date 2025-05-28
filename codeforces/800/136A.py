n = int(input())
arr = list(map(int, input().split()))  
_dict = {}
ans = []

for index, num in enumerate(arr):
    _dict[num] = index + 1
    

for i in range(n):
    print(_dict[i + 1], end=' ')


