def hoarse(arr, n, i, j):
    while True:
        while i < n:
            if arr[i]%2 != 0:
                i += 1
            
            else:
                break
        
        while j > 0:
            if arr[j]%2 == 0:
                j -= 1
            
            else:
                break
        
        if i >= j:
            return

        arr[i], arr[j] = arr[j], arr[i]

def rearrange(arr):
    res = []
    i = 0
    j = len(arr)-1

    if isPossible(arr, j+1):
        hoarse(arr, j, i, j)
    
    else:
        return "Rearrangement is not possible"

    while i <= j:
        res.append(arr[i])
        res.append(arr[j])

        i += 1
        j -= 1

    return res[:-1]

def isPossible(arr, n):
    even_num = sum(1 for num in arr if num % 2 == 0)
    odd_num = n-even_num

    if even_num == 0 or odd_num == 0 or abs(even_num - odd_num) <= 1:
        return True

    return False

arr = [2,1,6,4,5,7,7]
print(rearrange(arr))