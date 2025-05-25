from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
                
        print("Rn: ", nums)
        return k
    
sol = Solution()
print(sol.removeElement([1,2], 1))