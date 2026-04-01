class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0
        for i in nums:
            if i - 1 in seq:
                continue
            curr = 0
            j = i
            while j in seq:
                curr += 1
                j += 1
            res = max(res, curr)

        return res