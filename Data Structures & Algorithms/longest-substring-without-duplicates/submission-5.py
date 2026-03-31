class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        res = 0

        l = 0

        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            curr.add(s[r])

        return res
