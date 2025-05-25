def mySqrt(x):
    if x < 2:
        return x

    left = 1
    right = x // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right 

print(mySqrt(168888888888888888888888888888)) 
print(mySqrt(8))   