import math

class myMinHeap:
    def __init__(self, l=[]):
        self.arr = l
        # Build Heap
        # We need to start processing from the rightmost internal node only as the leaf nodes are already heaps.
        # We can get the rightmost internal node by getting the parent of last node
        # Since last node is len()-1
        # Parent node we get by (i-1)//2
        # So it will be (len()-2)//2
        i = (len(l) - 2) // 2

        while i >= 0:
            self.minHeapify(i)
            i = i - 1

    def parent(self, i):
        return (i - 1) // 2

    def lChild(self, i):
        return 2 * i + 1

    def rChild(self, i):
        return 2 * i + 2

    def insert(self, x):
        arr = self.arr
        arr.append(x)
        i = len(arr) - 1

        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p

    def minHeapify(self, i):
        arr = self.arr
        lt = self.lChild(i)
        rt = self.rChild(i)

        smallest = i
        n = len(arr)

        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt

        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)

    def extractMin(self):
        arr = self.arr
        n = len(arr)

        if n == 0:
            return math.inf
        res = arr[0]

        arr[0] = arr[n - 1]
        arr.pop()

        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):
        arr = self.arr
        arr[i] = x

        while i != 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]

            i = p

    def delete(self, i):
        n = len(self.arr)

        if i >= n:
            return

        else:
            self.decreaseKey(i, -math.inf)
            self.extractMin()
