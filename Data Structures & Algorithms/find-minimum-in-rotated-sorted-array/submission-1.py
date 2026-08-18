class Solution:
    def findMin(self, nums: List[int]) -> int:
        least = 1000
        for i in nums:
            if i < least:
                least = i
            
        return least