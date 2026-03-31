class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPal(i, j):
            l, r = i, j

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPal(i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.remove(s[i:j+1])

        dfs(0)
        return res
        