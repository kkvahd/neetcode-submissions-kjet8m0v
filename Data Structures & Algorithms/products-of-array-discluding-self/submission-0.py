class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]

        curr_prod = 1
        for i in range(len(nums)):
            res[i] = curr_prod
            curr_prod *= nums[i]
        
        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= curr_prod
            curr_prod *= nums[i]
        return res