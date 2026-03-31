class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            curr = [0 for i in range(26)]

            for c in s:
                curr[ord(c) - ord('a')] += 1

            curr = tuple(curr)
            if curr in group:
                group[curr].append(s)
            else:
                group[curr] = [s]

        return list(group.values())