n = int(input())

for i in range(n + 1, 10000):
    i_str = str(i)
    if len(set(i_str)) == 4:
        print(i)
        break
