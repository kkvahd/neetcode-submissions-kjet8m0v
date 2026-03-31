class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        stack = []

        for p, s in cars:
            t = (target - p) / s

            if not stack or t > stack[-1]:
                stack.append(t)
                continue

            stack.append(max(t, stack.pop()))

        return len(stack)

             