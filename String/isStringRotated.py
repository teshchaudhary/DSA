def isRotated(s1, s2):
    if len(s1) != len(s2):  # If lengths are not equal so these can't be rotations
        return -1

    temp = ""
    temp = s1+s1

    return temp.find(s2) != -1  # Find gives -1 when not found


print(isRotated("abcd", "cdab"))
