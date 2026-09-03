class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        max_p = 0

        for n in prices:
            minn = min(minn, n)
            max_p = max(max_p, n - minn)

        return max_p