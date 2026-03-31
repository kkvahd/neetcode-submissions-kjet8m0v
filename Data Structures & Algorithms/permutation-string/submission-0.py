class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True

        dict1 = {}
        for i in s1:
            dict1[i] = 1 + dict1.get(i, 0)

        l, r = 0, len(s1) - 1

        while r < len(s2):
            dict2 = {}
            for i in range(l, r+1):
                dict2[s2[i]] = 1 + dict2.get(s2[i], 0)
            if dict1 == dict2:
                return True
            
            l += 1
            r += 1
        return False
