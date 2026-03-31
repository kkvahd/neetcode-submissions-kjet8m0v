class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, subset, add):
            if add == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or add > target:
                return

            subset.append(nums[i])
            dfs(i, subset, add + nums[i])

            subset.pop()
            dfs(i + 1, subset, add)

        dfs(0, [], 0)
        return res