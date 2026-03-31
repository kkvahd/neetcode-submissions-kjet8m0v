class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        res = 0

        l = 0
        for i in range(len(height)):
            max_left[i] = l
            l = max(l, height[i])

        r = 0
        for i in range(len(height))[::-1]:
            max_right[i] = r
            r = max(r, height[i])

        for i in range(len(height)):
            w = min(max_left[i], max_right[i]) - height[i]
            res += max(0, w)

        return res