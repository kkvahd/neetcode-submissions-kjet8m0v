# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if not preorder or not inorder:
                return None

            curr = preorder[0]
            mid = inorder.index(curr)

            currNode = TreeNode(curr)

            currNode.left = build(preorder[1:mid+1], inorder[:mid])
            currNode.right = build(preorder[mid+1:], inorder[mid+1:])
            return currNode

        return build(preorder, inorder)
            