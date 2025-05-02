class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        sLargest = float('-inf')
        
        for i in range(len(arr)):
                    
            if largest < arr[i]:
                sLargest = largest
                largest = arr[i]
            
            if arr[i] < largest:
                sLargest = max(sLargest, arr[i])
            
        
        return sLargest if sLargest != float('-inf') else -1
