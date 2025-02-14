# Set  = [a,b,c]
# length = 3
# size = 2**3 = 8

# Run for binary counter = 000 to 111 (0,1,2,3,4,5,6,7)
# Value of Counter            Subset

#    000                    -> Empty set
#    001                    -> a
#    010                    -> b
#    011                    -> ab
#    100                    -> c
#    101                    -> ac
#    110                    -> bc
#    111                    -> abc

def getPowerSet1(str):
    l = len(str)
    size = 1<<l

    for i in range(size):
        for j in range(l):
            if (i & (1 << j )) != 0:
                print(str[j], end = "")
        
        print()

getPowerSet1("abc")

def getPowerSet2(str):
    l = len(str)
    size = 1 << l
    subsequences = []

    for i in range(size):
        subsequence = []
        for j in range(l):
            if (i & (1 << j)) != 0:
                subsequence.append(str[j])
        subsequences.append("".join(subsequence))

    return subsequences