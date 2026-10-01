class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #try to find target in O(log n )time
        #nums is not sorted in random order
        #i am guessing it has something to do with the amount of times it was sorted
        #you do left pointer on index 0 
        #right pointer last index
        #compare the 2 values

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
        return -1

