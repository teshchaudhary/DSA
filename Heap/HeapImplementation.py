import math


class myHead:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*i+1

    def rightChild(self, i):
        return 2*i+2

# O(log(N)), N is the number of element in the heap.
# First insert the element at the last of heap list.
# Now we have to maintain heap property.
# Compare the element with its parent and the swap if needed.
# We keep swapping until we find a node smaller the the element in case of a min heap.
# We also stop when we reach the root node.

    def insert(self, x):
        arr = self.arr
        arr.append(x)

        i = len(arr)-1

        while i > 0 and arr[self.parent(i)] > arr[i]:  # i > 0 means reaching root node
            # other condition checks until we get an element lesser than the key

            p = self.parent(i)  # returns the index of parent at the moment
            arr[i], arr[p] = arr[p], arr[i]  # swapping
            i = p  # moving i to the new position to be compared with grandparent and so on

    # To extract the minimum element from the heap we need two operations
    # One to get the minimum element out
    # Other one to heapify the remaining elements

    # To extract minimum from a heap in a O(1) complexity, we swap the first element(smallest in case of min heap) with the last element as pop from the list

    def minHeapify(self, i):
        arr = self.arr
        lt = self.leftChild(i)
        rt = self.rightChild(i)
        # Using it so that the recusion doesn't get to a place where the index is invalid
        n = len(arr)
        smallest = i  # Using the first node as the smallest initially

        # Making recursive calls to check which is the smallest among three (parent, leftchild, righchild)

        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt

        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt

        # if smallest is not i then we swap
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)

    def extractMin(self):
        arr = self.arr
        n = len(arr)

        if n == 0:
            return math.inf

        res = arr[0]

        arr[0] = arr[-1]  # No need of swapping
        arr.pop()

        self.minHeapify(0)
        return res

    # decreasing key value
    def decreaseKey(self, idx, val):
        arr = self.arr
        arr[idx] = val
        n = len(arr)

        while idx > 0 and arr[idx] < arr[self.parent(idx)]:
            p = self.parent(idx)
            arr[idx], arr[p] = arr[p], arr[idx]
            i = p

    # Delete Key
    def delete(self, i):
        n = len(self.arr)

        if i >= n:
            return

        else:
            self.decreaseKey(i, -math.inf)
            self.extractMin()
