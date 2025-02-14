# Get the sum of the given queries like
# getSum(0,3) => Get sum from index 0 to index 3 (both inclusive)
# getSum(3,9) => Get sum from index 3 to index 9 (both inclusive)

# O(n)
def func1(arr, si, ei):
    res = 0
    while si != ei+1:
        res += arr[si]
        si += 1
    
    return res

# arr = [2,8,3,9,6,5,4]
# print(func1(arr,0,6))

# For above solution we will be needing to process O(n) again and again
# This costs more time
# So we can preprocess data once for O(n) and then perform queries in O(1)

def preprocess(arr):
    l = len(arr)
    res = [None]*l
    res[0] = arr[0]

    for i in range(1, l):
        res[i] = res[i-1] + arr[i]
    
    return res

def func2(arr,si,ei):
    if si == 0:
        return preprocess(arr)[ei]
    else:
        return preprocess(arr)[ei] - preprocess(arr)[si-1]

arr = [2,8,3,9,6,5,4]
print(preprocess(arr))
print(func2(arr,1,2))