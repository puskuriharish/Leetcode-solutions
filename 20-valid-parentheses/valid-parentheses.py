class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        if len(s) == 1:
            return False
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                if mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
