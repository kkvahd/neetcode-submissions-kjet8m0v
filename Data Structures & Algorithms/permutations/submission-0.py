class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, picked, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for j in range(len(nums)):
                if j not in picked:
                    perm.append(nums[j])
                    picked.add(j)
                    dfs(j, picked, perm)
                    
                    perm.pop()
                    picked.remove(j)
            
        
        dfs(0, set({}), [])
        return res