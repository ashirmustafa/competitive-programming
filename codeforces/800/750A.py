
n, k = map(int, input().split())


total_time = 240


time_left = total_time - k


time_spent = 0
problems_solved = 0


for i in range(1, n + 1):
    time_needed = 5 * i
    time_spent += time_needed

  
    if time_spent > time_left:
        break

    problems_solved += 1


print(problems_solved)
