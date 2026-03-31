class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in set_nums:
                curr_num = n
                curr_len = 1
                while (curr_num + 1) in set_nums:
                    curr_len += 1
                    curr_num += 1
                res = max(res, curr_len)
        return res