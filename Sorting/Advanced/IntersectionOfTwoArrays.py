# The intersection of two arrays contains the elements common to both the arrays. The intersection should not count duplicate elements.
# Given two sorted arrays arr1[] and arr2[] of sizes N and M respectively. Find their intersection

def printIntersection(a, b, n, m):
        i = j = 0
        res = []
        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            
            elif a[i] > b[j]:
                j += 1
            
            else:
                if not res or a[i] != res[-1]:
                    res.append(a[i])
                
                i += 1
                j += 1
            
        return res
