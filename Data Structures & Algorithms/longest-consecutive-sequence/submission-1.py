class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for i in nums:
            curr = i
            if curr - 1 in num_set:
                continue
            curr_seq = 1
            while curr + 1 in num_set:
                curr_seq += 1
                curr += 1
            res = max(res, curr_seq)
        return res
            