class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s in set(['+', '-', '*', '/']):
                b, a = int(stack.pop()), int(stack.pop())
                if s == '+':
                    stack.append(a + b)
                elif s == '-':
                    stack.append(a - b)
                elif s == '*':
                    stack.append(a * b)
                else:
                    stack.append(a / b)
            else:
                stack.append(s)
        return int(stack[0])