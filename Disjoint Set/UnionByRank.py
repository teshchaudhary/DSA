# An optimization of Union Function
# In naive union operation in the worst case we can make chains of the connection

# Example
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5

# In the optimization, we can use one more array/list (Rank)
# This array stores the height of the tree, once a smaller rank disjoint set connects with a larger rank one then these both get connected, this prevents the chaining in the Tree

# Union by rank

n = 6
parent = [i for i in range(n)]
rank = [0 for i in range(n)]

def find(x) :
    if parent[x] == x :
        return x 
    return find(parent[x])
    
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

makeFriends(0,1)
makeFriends(1,3)
makeFriends(4,5)
makeFriends(4,2)

areFriends(4,3)