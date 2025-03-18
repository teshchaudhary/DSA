# An equillibrium point is when the sum of all the previous elements from a element is equal to the sum of the all next elements
# O(n^2)
def func1(arr):
    l = len(arr)
    for i in range(l):
        ls, rs = 0, 0

        for j in range(i):
            ls += arr[j]
        
        for k in range(i+1, len(arr)):
            rs += arr[k]

        
        if ls == rs:
            return True
    
    return False

arr = [3,4,8,-9,9,7]

print(func1(arr))

#O(n)

def func2(arr):
    tSum = sum(arr)
    lSum = 0

    for i in range(len(arr)):
        lSum += arr[i]

        if lSum == tSum:
            return i+1

        tSum -= arr[i]

    return -1