class Node:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        del self.cache[node.key]

    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev

        self.right.prev = node
        node.next = nxt

        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.insert(Node(key, value))
        
        if len(self.cache) > self.cap:
            self.remove(self.left.next)
