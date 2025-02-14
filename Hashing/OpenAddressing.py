class MyHash:
    def __init__(self, c):
        self.capacity = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, data):
        return data % self.capacity

    def search(self, data):
        h = self.hash(data)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == data:
                return True
            i = (i + 1) % self.capacity
            if i == h:
                return False
        return False

    def insert(self, data):
        if self.size == self.capacity:
            return False

        if self.search(data) == True:
            return False
        i = self.hash(data)
        t = self.table
        while t[i] not in (-1, -2):
            i = (i + 1) % self.capacity

        t[i] = data
        self.size = self.size + 1
        return True

    def remove(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i + 1) % self.capacity
            if i == h:
                return False
        return False


h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)
