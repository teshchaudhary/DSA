# Given three sorted arrays A, B and C of size N, M and P respectively. The task is to merge them into a single array which must be sorted in increasing order.


def mergeThree(self, A, B, C):
        res = []
    
        i = j = k = 0
        while i < len(A) or j < len(B) or k < len(C):
            if i < len(A):
                min_val = A[i]
            else:
                min_val = float('inf')
    
            if j < len(B) and B[j] < min_val:
                min_val = B[j]
    
            if k < len(C) and C[k] < min_val:
                min_val = C[k]
    
            res.append(min_val)
    
            if i < len(A) and min_val == A[i]:
                i += 1
            elif j < len(B) and min_val == B[j]:
                j += 1
            elif k < len(C) and min_val == C[k]:
                k += 1
    
        return res
