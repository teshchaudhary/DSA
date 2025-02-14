def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b, a%b)

def LCM(a,b):
    return (a*b)//gcd(a,b)

x,y = map(int, input().split())
print(gcd(x,y))
print(LCM(x,y))