# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inOrder(root):
            if not root:
                return []

            leftArr = inOrder(root.left)
            rightArr = inOrder(root.right)

            curr = []
            if leftArr:
                curr += leftArr
            
            curr.append(root)
            
            if rightArr:
                curr += rightArr

            return curr

        res = inOrder(root)

        return res[k-1].val