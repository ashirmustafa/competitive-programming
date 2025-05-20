def divide(dividend: int, divisor: int) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1


    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    is_negative = (dividend < 0) != (divisor < 0)


    a = abs(dividend)
    b = abs(divisor)
    result = 0

    for i in range(31, -1, -1):
        if (a >> i) >= b:
            result += 1 << i
            a -= b << i

    if is_negative:
        result = -result

    return result
