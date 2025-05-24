a, b = map(int, input().split())
is_limak_big = False
years = 0

while(is_limak_big == False):
    if a <= b:
        a = a*3
        b = b*2
        years += 1
        if a > b:
            is_limak_big = True
            break

print(years)