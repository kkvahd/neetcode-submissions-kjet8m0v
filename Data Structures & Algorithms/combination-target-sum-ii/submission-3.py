class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()

        def dfs(i, currSum):
            if currSum == target:
                res.append(comb.copy())
                return
                
            if i >= len(candidates) or currSum > target:
                return

            comb.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])

            comb.pop()
            j = i
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            
            dfs(j, currSum)

        dfs(0, 0)
        return res