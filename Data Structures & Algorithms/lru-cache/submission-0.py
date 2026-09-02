class Node: 
    def __init__(self, key, value):

        self.value = value
        self.key = key

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 


    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

        

    def put(self, key: int, value: int) -> None:
        # 1 add it 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # 2 delete LRU 
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


#   Cache
        # |key    |   1      |    2     |
        # |values | pointerA | pointerB | 


    # Initially:   right -> left 
    #                    <-

    #     right  -> nodeA -> nodeB -> left
