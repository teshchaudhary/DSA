# Check if a sum is being made by any pair
# Condition is elements are distinct

def sumExists(arr, sum):
    s = set(arr)
    for i in arr:
        diff = (sum-i)
        if diff in s and diff != i:
            return 1
    
    return 0

arr = [1,2,3,4,5,6,7,8,9,10]
addUp = 14

print(sumExists(arr,addUp))