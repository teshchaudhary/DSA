def reverseList(li):
    si = 0
    ei = len(li) - 1

    while si<ei:
        (li[si], li[ei]) = (li[ei], li[si])

        si+=1
        ei-=1
    
    return li

print(reverseList([1,2,3,4,5]))