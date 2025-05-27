n = int(input())

current = 0
max_people = 0

for _ in range(n):
    a, b = map(int, input().split())
    current = current - a + b
    if current > max_people:
        max_people = current

print(max_people)
