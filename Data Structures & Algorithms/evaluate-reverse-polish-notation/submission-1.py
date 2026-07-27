def add (x, y):
    return x + y

def sub (x, y):
    return x - y

def mul (x, y):
    return x * y

def div (x, y):
    return int(x / y)

ops = {
    '+': add, 
    '-': sub,
    '*': mul,
    '/': div
    }

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ops:
                y = stack.pop()
                x = stack.pop()
                stack.append(ops[t](x, y))
                continue
            else:
                stack.append(int(t))
        return stack[0]