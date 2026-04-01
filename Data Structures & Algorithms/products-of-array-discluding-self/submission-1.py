class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        for i in nums:
            prefix.append(pre)
            pre = pre * i

        postfix = [1 for i in nums]
        post = 1
        for i in range(len(nums))[::-1]:
            postfix[i] = post
            post = post * nums[i]

        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * postfix[i])

        return res