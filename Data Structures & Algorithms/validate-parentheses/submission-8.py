class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closetoopen = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for i in s:
            if stack and i in closetoopen and closetoopen[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0


        