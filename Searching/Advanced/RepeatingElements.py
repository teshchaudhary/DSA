# Every element will be present from 0-n if n is the maximum number in the array
# Only one element is repeated
# Find the repeating element

# O(n^2) if we check for every element
# O(nlogn) if we sort the array and check if the element is same as the next

# O(n) time and space complexity
def func(arr, n):
    visit = [False]*n
    for i in range(n):
        if visit[arr[i]]:
            return arr[i]

        visit[arr[i]] = True

    return -1


arr = [0, 1, 2, 2, 3, 4, 5]
print(func(arr, 7))
