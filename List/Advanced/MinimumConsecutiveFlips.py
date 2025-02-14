# Check the minimum bitflips required to make the whole array same
# If there is a group of same bits then we can flip them all at once
# Also tell the index of groups being made for it

# We can use the fact that if the first element and the last element of the binary array is same the difference between the group will be one otherwise 0

def func(arr):
    l = len(arr)
    for i in range(1, l):
        if arr[i-1] != arr[i]:
            if arr[i] != arr[0]:
                print(f"from {i} to", end=" ")

            else:
                print(f"{i-1}")

    if arr[-1] != arr[0]:
        print(l-1)


arr = [0, 0, 1, 1, 0, 0, 1, 1, 0]
func(arr)
