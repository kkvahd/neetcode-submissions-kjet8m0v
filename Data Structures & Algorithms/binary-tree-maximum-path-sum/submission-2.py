# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-1001]

        def dfs(root):
            if not root:
                return 0

            curr = root.val
            leftVal = dfs(root.left)
            rightVal = dfs(root.right)

            currSum = curr + max(0, leftVal) + max(0, rightVal)
            res[0] = max(res[0], currSum)
            return curr + max(0, max(leftVal, rightVal))

        dfs(root)
        return res[0]