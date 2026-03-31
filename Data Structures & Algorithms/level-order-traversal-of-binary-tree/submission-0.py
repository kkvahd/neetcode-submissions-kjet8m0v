# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}

        def traverse(root, level):
            if not root:
                return

            if level in res:
                res[level].append(root.val)
            else:
                res[level] = [root.val]
            
            traverse(root.left, 1 + level)
            traverse(root.right, 1 + level)

        traverse(root, 0)
        
        res_arr = []
        for i in res:
            res_arr.append(res[i])
        return res_arr