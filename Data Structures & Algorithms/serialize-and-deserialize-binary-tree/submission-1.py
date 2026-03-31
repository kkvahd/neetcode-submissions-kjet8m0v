# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfsPre(root):
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfsPre(root.left)
            dfsPre(root.right)

        dfsPre(root)
        return ",".join(res)
       

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        data = [i for i in data.split(",")]
        self.i = -1

        def build():
            if self.i >= len(data):
                return None

            self.i += 1
            val = data[self.i]

            if val == "N":
                return None

            root = TreeNode(data[self.i])

            root.left = build()
            root.right = build()

            return root

        return build()

            









