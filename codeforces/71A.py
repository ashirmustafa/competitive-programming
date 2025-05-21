n = int(input())

words = []

short_words = []

for _ in range(n):
    word = input()
    words.append(word)
    
for str in words:
    if len(str) > 10:
        short_words.append(f"{str[0]}{len(str)-2}{str[len(str)-1]}")
    else:
        short_words.append(str)

for str in short_words:
    print(str)


