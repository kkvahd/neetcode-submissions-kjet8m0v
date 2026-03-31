class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            this_val = nums[i]
            other_val = target - this_val
            if other_val in num_dict:
                return [num_dict[other_val], i]
            if this_val not in num_dict:
                num_dict[this_val] = i