class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertAfterHead(self, Node):
        Node.next = self.head.next
        Node.prev = self.head
        self.head.next.prev = Node
        self.head.next = Node

    def remove(self, Node):
        prev = Node.prev
        nxt = Node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node  = self.cache[key]
            self.remove(node)
            self.insertAfterHead(node)
            return node.value
        
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.insertAfterHead(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]