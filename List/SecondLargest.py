#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        i, l, h = -1, 0, len(arr)-1
        
        for j in range(l,h):
            if arr[j] > 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
           
        arr[i+1], arr[h] = arr[h], arr[i+1]
                