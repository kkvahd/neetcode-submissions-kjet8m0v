class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        l = 0
        curr_set = set()
        for r in range(len(s)):
            while s[r] in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[r])
            res = max(res, r - l + 1)

        return res