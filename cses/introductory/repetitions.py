str = str(input())

current_len, max_len = 1,1

for index in range(1, len(str)):
    if str[index] == str[index - 1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1
        
print(max_len)