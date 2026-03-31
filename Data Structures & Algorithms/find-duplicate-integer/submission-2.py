class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for curr in nums:
            index = abs(curr) - 1

            if nums[index] < 0:
                return abs(curr)

            nums[index] *= -1
        return -1
