class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        test = {}

        for i, n in enumerate(nums):
            answer = target - n
            if answer in test:
                return [test[answer], i]
            test[n] = i
        return -1