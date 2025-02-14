#Naive Solution
# O(n^2)
def leftmost1(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return i
    
    return -1

# O(n)
def leftmost2(st) :
    count = [0] * 26
    for i in range(len(st)) :
        count[ord(st[i] - 97)] += 1 

    for i in range(len(st)) :
        if count[ord(st[i] - 97)] > 1:
            return i 
        
    return -1 

# O(n)
def leftmost3(st):
    vis = [False]*26

    for i in range(len(st)) :
        if vis[ord(st[i] - 97)] == True:
            return i
        
        else:
            vis[ord(st[i] - 97)] = True
    
    return -1

# O(n)

def leftmost4(st):
    fIndex = [-1] * 26
    res = float['inf']

    for i in range(len(st)):
        if fIndex[ord(i) - 97] != -1:
            fIndex[ord(i) - 97] = i
        
        else:
            res = min(res, fIndex[ord(i) - 97])

    if res != float['inf']:
        return res
    
    else:
        return -1
    

