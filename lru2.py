class Node():
    def __init__(self, key, val) -> None:
        self.next = self.prev = None
        self.key = key
        self.val = val

    def __repr__(self):
        return f"Node(key={self.key},val={self.val})"

class LRUCache():
    def __init__(self, capacity: int) -> None:
        self.cache: dict[int, Node] = {}
        self.capacity = capacity
        self.left = Node(None,None)
        self.right = Node(None,None)
        self.left.next = self.right
        self.right.prev = self.left

    def remove_from_queue(self, node:Node) -> None:
        #left -> new_node -> right
        node.prev.next = node.next
        node.next.prev = node.prev


    def add_to_queue(self, node:Node) -> None:
        mru = self.right.prev
        mru.next = node
        node.prev = mru
        node.next = self.right
        self.right.prev = node

    def get(self, key:int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_queue(node)
            self.add_to_queue(node)
            return node.val
        else:
            return -1

    def put(self, key:int, value:int) -> None:
        node = Node(key, value)
        if key in self.cache:
            self.remove_from_queue(self.cache[key])
        self.cache[key] = node
        self.add_to_queue(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_from_queue(lru)
            del self.cache[lru.key]


# op = ["put","put"]
# input = [[1,1],[2,2]]
op = ["put","put","get","put","get","put","get","get","get"]
input = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

lru = LRUCache(2)
z = zip(op,input)
for x in z:
    op = x[0]
    i = x[1]
    if op == 'put':
        lru.put(i[0],i[1])
    else:
        lru.get(i[0])
    print('op ', op,' input ', i, ' current cache ', lru.cache)

