# Anagram refers to a string that is a permutation of another string

def isAnagram(s1, s2):

    i = 0
    j = 0

    count = [0]*256

    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    
    for i in count:
        if i!= 0:
            return False
    
    return True

print(isAnagram("acer","race"))