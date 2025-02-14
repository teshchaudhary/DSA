def isPalindrome(s):
    si = 0
    ei = len(s) - 1

    while si < ei:
        if s[si] != s[ei]:
            return False

        si += 1
        ei -= 1

    return True


print(isPalindrome("abbaa"))
