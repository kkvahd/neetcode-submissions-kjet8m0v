class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resLen = float("inf")
        res = []
        want, have = {}, {}
        
        for i in t:
            want[i] = 1 + want.get(i, 0)

        wantCount, haveCount = len(want), 0
        

        l = 0
        for r in range(len(s)):
            have[s[r]] = 1 + have.get(s[r], 0)

            if s[r] in want and want[s[r]] == have[s[r]]:
                haveCount += 1

            while haveCount == wantCount:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                have[s[l]] -= 1
                if s[l] in want and want[s[l]] > have[s[l]]:
                    haveCount -= 1
                l += 1
        return s[res[0]:res[1]+1] if resLen != float("inf") else ""
        

        