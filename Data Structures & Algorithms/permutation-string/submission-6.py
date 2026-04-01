class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        want = [0] * 26
        have = [0] * 26

        for i in s1:
            want[ord(i) - ord('a')] += 1

        for i in range(len(s1)):
            c = s2[i]
            have[ord(c) - ord('a')] += 1

        if want == have:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            have[ord(s2[r]) - ord('a')] += 1
            have[ord(s2[r - len(s1)]) - ord('a')] -= 1

            if want == have:
                return True
        return False
        