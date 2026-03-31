class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, subset):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            subset.append(nums[i])
            dfs(i, total + nums[i], subset)

            subset.pop()
            dfs(i + 1, total, subset)

        dfs(0, 0, [])
        return res