class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # stores only indices: int

        for i, n in enumerate(temperatures): 
            while stack and n > temperatures[stack[-1]]:
                test = stack.pop()
                res[test] = i - test   
            stack.append(i)
        return res