# Naive Solution

# def func(arr):
#     for i in range(len(arr)):
#         flag = False

#         # Checks if the element is appeared before or not

#         for j in range(i):
#             if arr[i] == arr[j]:
#                 flag = True
#                 break

#         # If it has appeared then skip
#         if flag == True:
#             continue

#         # If not then check in the array and give the frequency of the element
#         freq = 1
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j]:
#                 freq += 1

#         print(arr[i], freq)


def func(arr):
    d = {}
    for i in arr:
        if i in d.keys():
            d[i] += 1

        else:
            d[i] = 1
    return d


print(func([1, 2, 1, 2, 1, 2, 1, 2, 3]))
