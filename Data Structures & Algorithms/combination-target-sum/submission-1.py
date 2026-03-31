class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currSum, subset):
            if i >= len(nums) or currSum > target:
                return

            if currSum == target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i, currSum + nums[i], subset)

            subset.pop()
            dfs(i + 1, currSum, subset)

        dfs(0, 0, [])
        return res

            