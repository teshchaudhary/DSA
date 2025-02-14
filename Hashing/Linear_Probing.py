def LinearProbing(hashSize, arr):
    table = [-1] * hashSize

    for data in arr:
        iniKey = data % hashSize

        for i in range(hashSize):
            key = (iniKey+i) % hashSize

            if table[key] == -1:
                table[key] = data
                break

            elif table[key] == data:
                break

    return table


hashSize = 10
N = 4
arr = [4, 14, 24, 44]

print(LinearProbing(hashSize, arr, N))


def printNonRepeated(self,arr,n):

        s = {}
        for i in arr:
            count = 1
            if i in s:
                val = s[i]
                count += val
            s[i] = count
        
        l = []

        for key in arr:
            if s[key] == 1:
                l.append(i)
        
        return l