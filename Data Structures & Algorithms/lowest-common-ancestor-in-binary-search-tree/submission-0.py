# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = [None]

        def dfs(root):
            if root == None:
                return


            if root.val > p.val and root.val > q.val:
                dfs(root.left)
            elif root.val < p.val and root.val < q.val:
                dfs(root.right)
            else:
                res[0] = root

            return

        dfs(root)
        return res[0]
