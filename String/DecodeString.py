# eg:  "3[b2[ca]]"
# Output: "bcacabcacabcaca"

def decodedString(s):
    stack=[]
    
    for i in s:
        if i != "]":
            stack.append(i)
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            
            stack.pop()
            
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            
            stack.append(int(num)*substr)
        
    return "".join(stack)