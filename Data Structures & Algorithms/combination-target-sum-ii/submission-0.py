class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])

            subset.pop()
            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1

            dfs(j, subset, total)

        dfs(0, [], 0)
        return res