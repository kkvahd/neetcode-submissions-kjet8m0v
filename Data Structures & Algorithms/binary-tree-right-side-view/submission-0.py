# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque()
        res = []
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                curr = q.popleft()

                if i == qLen - 1:
                    res.append(curr.val)
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
            print([i.val for i in level])
            for i in level:
                q.append(i)
        return res