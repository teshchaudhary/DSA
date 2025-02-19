def isIdentical(T, S):
    if T is None and S is None:
        return True
    
    if T is None or S is None:
        return False

    return T.data == S.data and isIdentical(T.left, S.left) and isIdentical(T.right, S.right)
    
def isSubTree(T, S):
    if not S:
        return True 
    
    if not T:
        return False
    
    elif isIdentical(T,S):
        return True
    
    else:
        return isSubTree(T.left ,S) or isSubTree(T.right, S)
