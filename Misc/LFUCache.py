class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}     # key -> Node
        self.freq_map = {}  # freq -> (head, tail) of DLL
        self.min_freq = 0

    def _create_list(self, freq):
        head = Node(-1, -1)
        tail = Node(-1, -1)
        head.next = tail
        tail.prev = head
        self.freq_map[freq] = (head, tail)

    def _remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        head, tail = self.freq_map[node.freq]
        if head.next == tail:  # list empty
            del self.freq_map[node.freq]
            if node.freq == self.min_freq:
                self.min_freq += 1

    def _add(self, node):
        freq = node.freq
        if freq not in self.freq_map:
            self._create_list(freq)
        head, _ = self.freq_map[freq]
        node.next = head.next
        node.prev = head
        head.next.prev = node
        head.next = node

    def _update(self, node):
        self._remove(node)
        node.freq += 1
        self._add(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove LRU node from min_freq list
                head, tail = self.freq_map[self.min_freq]
                lru = tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.min_freq = 1
            self._add(new_node)