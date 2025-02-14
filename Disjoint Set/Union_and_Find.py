n = 6
parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    
    return find(parent[x])

def makeFriends(x, y): # Union
    x_representative = find(x)
    y_representative = find(y)

    if x_representative == y_representative:
        return
    
    parent[y_representative] = x_representative

def areFriends(x,y):
    print(find(x) == find(y))

makeFriends(0,1)
makeFriends(1,3)
makeFriends(4,5)
makeFriends(4,2)

areFriends(4,3)