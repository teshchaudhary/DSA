class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def separateChaining(hashSize, arr):
    hashtable = [[]for i in range(hashSize)]
        
    for data in arr:
        key = data % hashSize
        if len(hashtable[key]) == 0:
            head = Node(data)
            tail = head
            hashtable[key].append(head)
        else:
            newNode = Node(data)
            tail.next = newNode
            tail = newNode
        
    return hashtable

def printing(table):
    for i in table:
        while 