class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(houses):
            n = len(houses)
            dp = [0] * (n + 1)

            dp[0] = 0
            dp[1] = houses[0]

            for i in range(2, n + 1):
                dp[i] = max(
                    dp[i - 1],
                    houses[i - 1] + dp[i - 2]
                )

            return dp[n]

        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )