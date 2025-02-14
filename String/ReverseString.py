def reverseString(s):
    rev = ""
    for i in s:
        rev = i + rev

    return rev


print(reverseString("hello"))
