n = 6
parent = [i for i in range(n)]
rank = [0 for i in range(n)]

# Path Compression
def find(x) :
    if parent[x] == x :
        return x 
    parent[x] = find(parent[x])
    return parent[x]

# Union by Rank
def makeFriends(x,y) :
    x_rep = find(x)
    y_rep = find(y)
    if (x_rep == y_rep) :
        return 
    
    if (rank[x_rep] < rank[y_rep]) :
        parent[x_rep] = y_rep

    elif (rank[x_rep] > rank[y_rep]) :
        parent[y_rep] = x_rep

    else :
        parent[y_rep] = x_rep
        rank[x_rep] += 1 
        
    return (parent,rank)

def areFriends(x,y):
    print(find(x) == find(y))