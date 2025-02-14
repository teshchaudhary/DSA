# Direct Methods

# Method 1

# def leftRotation(arr, d):
#     arr = arr[d:] + arr[:d]
#     return arr


# arr = [1, 2, 3, 4, 5]
# arr = leftRotation(arr, 2)

# print(arr)

# Method 2

# from collections import deque
# def leftRotation(arr, d):
#     dq = deque(arr)
#     dq.rotate(-d)  # -d means left rotation while d means right rotation
#     l = list(dq)
#     return l


# arr = [1, 2, 3, 4, 5]
# arr = leftRotation(arr, 2)

# print(arr)

# Logical Methods

# Method 1

def lrotate(arr, d):
    for _ in range(d):
        arr.append(arr.pop(0))


arr = [1, 2, 3, 4, 5]
lrotate(arr, 3)
print(arr)

# Method 2


def reverse(arr, b, e):
    while b < e:
        arr[b], arr[e] = arr[e], arr[b]
        b = b+1
        e = e-1


def leftRotate(arr, d):
    if d == 0:  # Case when we don't need to rotate
        return arr

    else:
        n = len(arr)
        d = d % n  # Handles when we need to rotate more than the length of list
        # If number is already smaller then d remains same

        reverse(arr, 0, d-1)
        reverse(arr, d, n-1)
        reverse(arr, 0, n-1)


l = [10, 20, 30, 40, 50]
leftRotate(l, 3)
print(l)
