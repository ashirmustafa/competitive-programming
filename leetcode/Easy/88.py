from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    
    Merge nums2 into nums1 in non-decreasing order.
    nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
    The first m elements of nums1 are valid; the rest are zeros as placeholders.
    """
    # Write your code here
    pass

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Expected output: [1, 2, 2, 3, 5, 6]
