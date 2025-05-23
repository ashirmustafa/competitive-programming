def number_spiral(row, col):
    if row > col:
        if row % 2 == 1:
            return (row - 1)**2 + col
        else:
            return row**2 - col + 1
    else:
        if col % 2 == 0:
            return (col - 1)**2 + row
        else:
            return col**2 - row + 1


t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    print(number_spiral(r, c))
