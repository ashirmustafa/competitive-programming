from typing import List

n, max_h = map(int, input().split())
all_h = list(map(int, input().split()))

total_width = 0

for h in all_h:
    if h > max_h:
        total_width = total_width + 2
    else:
        total_width = total_width + 1
        
print(total_width)