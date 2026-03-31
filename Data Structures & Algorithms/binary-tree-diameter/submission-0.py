# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def diameter(root):
            if not root:
                return 0

            left_depth = diameter(root.left)
            right_depth = diameter(root.right)

            curr_dia = left_depth + right_depth
            res[0] = max(res[0], curr_dia)

            return 1 + max(left_depth, right_depth)

        diameter(root)
        return res[0]
        