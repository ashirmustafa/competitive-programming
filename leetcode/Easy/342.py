class Solution:
    def divide(self, n) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0
    
sol = Solution()
print(sol.divide(15))