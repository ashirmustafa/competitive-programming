n = int(input())
numbers = list(map(int, input().split()))

total = n * (n + 1) // 2
current_sum = sum(numbers)

print(total - current_sum)
