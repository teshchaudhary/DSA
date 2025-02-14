def QuadraticProbing(hashSize, arr):
    table = [-1] * hashSize
    for data in arr:
        iniKey = data % hashSize

        for i in range(hashSize):
            key = (iniKey+(i)**2) % hashSize
        
            if table[key] == -1:
                table[key] = data
                break
                
            elif table[key] == data:
                break
                
    return table

hashSize = 11
arr = [21,10,32,43]
print(QuadraticProbing(hashSize, arr))