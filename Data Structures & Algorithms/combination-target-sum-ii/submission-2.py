class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort()

        def dfs(i, add):
            if add == target:
                res.append(combo.copy())
                return

            if add > target or i >= len(candidates):
                return

            combo.append(candidates[i])
            dfs(i + 1, add + candidates[i])

            combo.pop()
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1

            dfs(j, add)

        dfs(0, 0)
        return res