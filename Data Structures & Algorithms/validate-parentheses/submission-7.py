opens = {'}': '{', ']': '[', ')': '('}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['[', '(', '{']:
                stack.append(i)
                continue
            
            if not stack:
                return False
            x = stack.pop()
            if x != opens[i]:
                return False
        return not stack