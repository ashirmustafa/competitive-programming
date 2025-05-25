from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans
    
sol = Solution()
print(sol.getConcatenation([1,2,1]))