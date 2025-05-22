n = int(input())
run = True
while ( run == True ):
    print(n)
    if( n == 1):
        run = False
    if(n % 2 == 0):
       n = n // 2
    else:
        n = (n * 3) + 1

