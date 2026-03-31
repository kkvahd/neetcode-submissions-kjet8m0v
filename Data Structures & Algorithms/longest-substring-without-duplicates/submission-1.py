class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 0

        for l in range(len(s)):
            curr_set = set([s[l]])
            r = l + 1
            while r < len(s) and s[r] not in curr_set:
                curr_set.add(s[r])
                r += 1
            res = max(res, r - l)
        return res

        