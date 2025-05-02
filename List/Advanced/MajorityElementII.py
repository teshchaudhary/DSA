class Solution:
    def findMajority(self, arr):
        n = len(arr)
        candidate_1 = 0
        candidate_2 = 0
        votes_1 = 0
        votes_2 = 0
        
        for candidate in arr:
            if candidate == candidate_1:
                votes_1 += 1
            
            elif candidate == candidate_2:
                votes_2 += 1
            
            elif votes_1 == 0:
                candidate_1 = candidate
                votes_1 = 1
            
            elif votes_2 == 0:
                candidate_2 = candidate
                votes_2 = 1
            
            else:
                votes_1 -= 1
                votes_2 -= 1
        
        res = []
        v_1, v_2 = 0, 0
        
        for candidate in arr:
            if candidate == candidate_1:
                v_1 += 1
            
            elif candidate == candidate_2:
                v_2 += 1
        
        if v_1 > (n//3):
            res.append(candidate_1)
        if v_2 > (n//3):
            res.append(candidate_2)
        
        res.sort()
        return res