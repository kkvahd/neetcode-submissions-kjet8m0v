class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = a + nums[l] + nums[r]

                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])

                    left_val = nums[l]
                    right_val = nums[r]

                    while l < r and nums[l] == left_val:
                        l += 1
                    while r > l and nums[r] == right_val:
                        r -=1
        return res
       