class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s1) > len(s2):
            return False

        need = [0 for i in range(26)]
        curr = [0 for i in range(26)]

        for i in s1:
            need[ord(i) - ord('a')] += 1
        for i in range(len(s1)):
            curr[ord(s2[i]) - ord('a')] += 1

        if need == curr:
            return True

        for i in range(len(s1), len(s2)):
            curr[ord(s2[i]) - ord('a')] += 1
            curr[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if curr == need:
                return True

        return False