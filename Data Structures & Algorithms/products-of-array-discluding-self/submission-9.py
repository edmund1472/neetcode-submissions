class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total *= num

        res = []

        for num in nums:
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)

        return res