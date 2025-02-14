class hashmap:
    def __init__(self,b):
        self.bucket = b
        self.l = [[] for _ in range(b)]

    def insert(self, data):
        key = data % self.bucket
        self.l[key].append(data)
    
    def delete(self, data):
        key = data % self.bucket
        if data in self.l[key]:
            self.l[key].remove(key)
    
    def search(self, data):
        key = data % self.bucket
        return data in self.l[key]

h = hashmap(7)
h.insert(14)
h.insert(15)
h.insert(16)
h.insert(17)
h.insert(18)
h.insert(19)

print(h.search(20))