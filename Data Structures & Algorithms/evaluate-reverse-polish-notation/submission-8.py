class Solution:
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in self.operators:
                second = stack.pop()
                first = stack.pop()
                result = self.operators[token](first, second)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
            
            
        