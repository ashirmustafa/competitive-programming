class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2147483648
        INT_MAX = abs(INT_MIN) - 1
        
        quotient = 0
        
        is_negative = False
        if (dividend < 0) != (divisor < 0):
            is_negative = True

            
        a = abs(dividend)
        b = abs(divisor)
        
        for i in range(31, -1, -1):
            if ( a >> i) >= b:
                quotient = quotient + (1 << i)
                a = a - (b << i)
                
        if is_negative == True:
            quotient = -quotient
                
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX   
        
        return quotient     
        

                
        
sol = Solution()
# sol.divide(10,3)
print(sol.divide(-2147483648,1))
# print(sol.divide(7,-3))
        
