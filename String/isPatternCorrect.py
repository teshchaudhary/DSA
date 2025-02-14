def isCorrect(s):

    if len(s) < 10:
        return 0
    nc = 0
    uc = 0
    lc = 0
    sc = 0

    i = 0
    while i < len(s):
        if s[i] in "0123456789":
            nc += 1

        elif 65 <= ord(s[i]) <= 90:
            uc += 1

        elif 97 <= ord(s[i]) <= 122:
            lc += 1

        elif s[i] in "@#$-*":
            sc += 1

        i += 1

    if nc == 0 or uc == 0 or lc == 0 or sc == 0:
        return 0

    else:
        return 1
