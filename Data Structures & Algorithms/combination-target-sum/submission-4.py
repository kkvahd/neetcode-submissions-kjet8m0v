class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, currSum):
            if i >= len(nums):
                return
            
            if currSum > target:
                return

            if currSum == target:
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i, currSum + nums[i])

            curr.pop()
            dfs(i + 1, currSum)

        dfs(0, 0)
        return res