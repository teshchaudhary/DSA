class Solution:
    def findSubString(self, str):
        unique_characters = len(set(str))
        d =  dict()
        current_unique_characters = 1
        res = float('inf')
        
        i = 0
        d[str[i]] = 1
        for j in range(1, len(str)):
            if str[j] not in d:
                d[str[j]] = 1
                current_unique_characters += 1
            
            else:
                d[str[j]] += 1
            
            while current_unique_characters == unique_characters:
                res = min(res, j-i+1)
                d[str[i]] -= 1
                
                if not d[str[i]]:
                    current_unique_characters -= 1
                    del d[str[i]]
                    
                i += 1
        
        return res