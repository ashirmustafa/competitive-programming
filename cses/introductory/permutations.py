n = int(input())

even_list = []
odd_list = []
result = []
if n == 1:
    print(n)
elif n <= 3 and n > 1:
    print("NO SOLUTION")
else:
    for i in range(1,n+1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    
    result = even_list + odd_list
    print(*result)
