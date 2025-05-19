from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = bin(n)[2:]
        count_even = 0
        count_odd = 0
        reversed_binary = binary[::-1]
        print(binary)
        for index, bit in enumerate(reversed_binary):
            if bit == '1':
                if index % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        
        return [count_even, count_odd]
        
                

            
    

sol = Solution()
print(sol.evenOddBit(50))
