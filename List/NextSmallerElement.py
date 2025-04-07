def nextSmallerElement(arr, n):
    res = [-1 for _ in range(n)]
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            res[i] = stack[-1]

        stack.append(arr[i])
    
    return res
