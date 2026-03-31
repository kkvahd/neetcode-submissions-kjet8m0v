class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        picked = set({})

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for n in nums:
                if n not in picked:
                    subset.append(n)
                    picked.add(n)
                    dfs()

                    subset.pop()
                    picked.remove(n)
        
        dfs()
        return res