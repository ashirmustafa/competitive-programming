import math
m, n, a = map(int, input().split())

for_length = 0
for_width = 0

for_length = math.ceil(m / a)
for_width = math.ceil(n / a)
print(for_length * for_width)

