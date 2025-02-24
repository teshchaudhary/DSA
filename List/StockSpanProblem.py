def calculateSpan(arr):
    n = len(arr)
    stack = []
    res = []
    
    for i in range(n):
        res[i] = 1
            
        while stack and arr[stack[-1]] <= arr[i]:
            a = stack.pop()
            res[i] += res[a]
    
        stack.append(i)

    return res