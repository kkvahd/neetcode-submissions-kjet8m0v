# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, lower, upper):
            if not root:
                return True

            curr = root.val

            isCurrValid = curr > lower and curr < upper

            return isCurrValid and dfs(root.left, lower, curr) and dfs(root.right, curr, upper)

        return dfs(root, float("-inf"), float("inf"))
        
            