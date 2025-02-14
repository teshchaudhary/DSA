# def DtB(n):
#     while n>0:
#         if n%2!=0:
#             print(1, end = "")
#         else:
#             print(0, end = "")
#         n//=2

# DtB(21)

def DtB(n):
    while n > 0:
        if n & 1 != 0:
            print(1, end="")
        else:
            print(0, end="")
        n = n >> 1


DtB(15)


# right shit 1 is divide by 2
# left shift 1 is multiply by 2
