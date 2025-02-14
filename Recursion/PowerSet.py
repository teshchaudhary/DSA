def generator(s,curr,idx,l):
    if idx == len(s):
        l.append(curr)
        return
    
    generator(s,curr+s[idx],idx+1,l)
    generator(s,curr,idx+1,l)


def powerSet(s):
    l = []
    generator(s, "", 0, l)
    
    return l