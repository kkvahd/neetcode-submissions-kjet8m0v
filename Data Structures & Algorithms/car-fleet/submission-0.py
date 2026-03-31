class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            t = (target - p)/s
            if not stack:
                stack.append(t)
            else:
                if t <= stack[-1]:
                    continue
                else:
                    stack.append(t)
        return len(stack) 