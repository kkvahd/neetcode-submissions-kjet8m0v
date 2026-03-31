# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = [True]


        def dfs(a, b):
            if (not a) and (not b):
                return
                
            if (not a and b) or (not b and a):
                same[0] = False
                return

            if a.val != b.val:
                same[0] = False
                return

            dfs(a.left, b.left)
            dfs(a.right, b.right)

        dfs(p, q)
        return same[0]