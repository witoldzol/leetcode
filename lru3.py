class Node:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        # dll (LRU)-> node_1 ... node_n <-(MRU)
        self.left = Node()
        self.right = Node()
        # init (LRU)-> <-(MRU)
        self.left.next = self.right
        self.right.prev = self.left

    def remove_from_queue(self, node: Node) -> None:
        # left => node => right
        node.prev.next = node.next
        # left <= node <= right
        node.next.prev = node.prev

    def insert_to_queue(self, node: Node) -> None:
        # node => right
        # node ....=> new_node <= right
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def put(self, key: int, val: int) -> None:
        node = Node(key, val)
        # insert into dll
        self.insert_to_queue(node)
        # insert into cache !
        self.cache[key] = node
        # remove if over capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_from_queue(lru)
            del self.cache[lru.key]

    def get(self, key: int) -> int:
        if key in self.cache:
            # update LRU
            node = self.cache[key]
            self.remove_from_queue(node)
            self.insert_to_queue(node)
            return node.val
        return -1

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

