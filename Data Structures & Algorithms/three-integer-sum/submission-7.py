class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for curr in range(len(nums)):
            if nums[curr] > 0:
                break
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue
            l = curr + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[curr] + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    res.append([nums[curr], nums[l], nums[r]])
                    
                    left_val = nums[l]
                    right_val = nums[r]

                    while l < r and nums[l] == left_val:
                        l += 1
                    while r > l and nums[r] == right_val:
                        r -= 1

        return res
