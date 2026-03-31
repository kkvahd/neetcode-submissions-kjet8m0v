class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, total, subset):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i], subset)

            subset.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            dfs(j, total, subset)

        dfs(0, 0, [])
        return res