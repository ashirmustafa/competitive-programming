from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = 0
        for i in range(m, m + n):
            if p > n - 1:
                p = p + 1
                break
            else:
                nums1[i] = nums2[p]
                p += 1
        nums1.sort()
        pass


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)  