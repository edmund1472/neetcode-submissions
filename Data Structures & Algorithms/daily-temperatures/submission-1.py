class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # stores only indices: int

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append(i)

        return res