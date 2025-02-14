def PalindromeNumber(n):
    rev = 0
    temp = n

    while temp%10 != 0:
        ud = temp%10
        rev = rev*10+ud
        temp//=10
    
    return rev == n

print(PalindromeNumber(1218))