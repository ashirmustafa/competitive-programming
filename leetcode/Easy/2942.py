from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i in range(len(words)):
            if x in words[i]:
                indices.append(i)
                
        return indices
    
sol = Solution()
print(sol.findWordsContaining(["leet","code"], "e")) 
print(sol.findWordsContaining(["leet","code"], "l")) 