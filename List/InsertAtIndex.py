def insertAtIndex(arr, index, element):
    arr.append(0)

    i = len(arr)-1

    while i > index-1:
        arr[i] = arr[i-1]
        i -= 1
    arr[index] = element

arr = [1,2,3,4,5]
insertAtIndex(arr, 0, 99)
print(arr)