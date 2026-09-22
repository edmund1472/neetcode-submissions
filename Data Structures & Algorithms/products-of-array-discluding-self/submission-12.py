class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_nums = [0] * len(nums)
        r_nums = [0] * len(nums)
        l_mult = 1
        r_mult = 1
        
        

        n = len(nums)

        i = 0
        j = len(nums) - 1

        for i in range(len(nums)):
            l_nums[i] = l_mult
            r_nums[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

            i += 1
            j -= 1
        
        res = []
        for i in range(n):
            res.append(l_nums[i] * r_nums[i])
        return res 