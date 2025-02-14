def quadraticRoots(a, b, c):
    l = []
    d = (b**2) - (4*a*c)
    
    if d < 0:
        l.append(-1)
        return l
    else:
        d = d**(1/2)
        r1 = int((((-b) + d) // (2*a)))
        r2 = int((((-b) - d) // (2*a)))
        l.append(max(r1,r2))
        l.append(min(r1,r2))
        
        
        return l

print(quadraticRoots(1,-7,12))