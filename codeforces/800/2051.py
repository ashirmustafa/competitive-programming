t = int(input())

for _ in range(t):
    n, a, b, c = map(int, input().split())
    cycle = [a, b, c]
    cycle_sum = a + b + c

    # calculate how many full 3-day cycles we can skip
    full_cycles = (n // cycle_sum) * 3
    total = (n // cycle_sum) * cycle_sum
    day = full_cycles
    index = 0

    # now simulate only the remaining few days
    while total < n:
        total += cycle[index]
        index = (index + 1) % 3
        day += 1

    print(day)
