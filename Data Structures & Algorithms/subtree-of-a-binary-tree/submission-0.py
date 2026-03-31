# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def dfs(main, sub):
            if not main and not sub:
                return True
                
            if main and sub and main.val == sub.val:
                return dfs(main.left, sub.left) and dfs(main.right, sub.right)
            else:
                return False


        arr = []
        def dfs_main(root):
            if not root:
                return
                
            arr.append(root)
            dfs_main(root.left)
            dfs_main(root.right)

        dfs_main(root)
        
        for i in arr:
            val = dfs(i, subRoot)
            res = res or val

        return res