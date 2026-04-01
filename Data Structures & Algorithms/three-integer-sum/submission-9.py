class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m = l + 1
            r = len(nums) - 1

            while m < r:
                add = nums[l] + nums[m] + nums[r]
                if add > 0:
                    r -= 1
                elif add < 0:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])

                    leftVal = nums[m]
                    rightVal = nums[r]
                    while m < r and nums[m] == leftVal:
                        m += 1
                    while r > l and nums[r] == rightVal:
                        r -= 1

        return res