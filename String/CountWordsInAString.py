def countWords(s):
    count = 0
    for i in s.split():
        count += 1

    return count


print(countWords("abba"))
