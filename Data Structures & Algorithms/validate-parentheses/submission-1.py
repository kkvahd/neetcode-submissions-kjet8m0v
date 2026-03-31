class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()

                if (popped == '(' and c == ')') or (popped == '[' and c == ']') or (popped == '{' and c == '}'):
                    continue
                else:
                    return False

        return len(stack) == 0