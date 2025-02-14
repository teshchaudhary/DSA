def twoPointerApproach(arr, target_sum, si):
    l = len(arr)
    ei = l - 1

    while si < ei:

        if arr[si] + arr[ei] > target_sum:
            ei -= 1

        elif arr[si] + arr[ei] < target_sum:
            si += 1

        elif arr[si] + arr[ei] == target_sum:
            return True

    return False


def func1(arr, target_sum):
    for i in range(len(arr)-2):
        if twoPointerApproach(arr, target_sum-arr[i], i+1):
            return True

    return False


arr = [1, 2, 3, 4, 5]
print(func1(arr, 5))
