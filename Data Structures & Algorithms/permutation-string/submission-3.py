class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        want = [0 for i in range(26)]
        have = [0 for i in range(26)]

        if len(s1) > len(s2):
            return False
             
        for i in range(len(s1)):
            want[ord(s1[i]) - ord('a')] += 1

        for i in range(len(s1)):
            have[ord(s2[i]) - ord('a')] += 1

        if want == have:
            return True

        for i in range(len(s1), len(s2)):
            have[ord(s2[i]) - ord('a')] += 1
            have[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if want == have:
                return True

        return False