class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return float("inf")

            if remaining in memo:
                return memo[remaining]

            best = float("inf")

            for coin in coins:
                best = min(best, 1 + dfs(remaining - coin))

            memo[remaining] = best
            return best

        answer = dfs(amount)

        return answer if answer != float("inf") else -1