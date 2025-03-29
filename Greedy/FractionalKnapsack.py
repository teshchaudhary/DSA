class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        n = len(val)
        value_per_weight = []
        
        for i in range(n):
            value_per_weight.append([val[i]/wt[i], i])
            
        value_per_weight.sort(reverse = True)
        res = 0
        for i in range(n):
            j = value_per_weight[i][1]
            
            if wt[j] <= capacity:
                res += val[j]
                capacity -= wt[j]
            
            else:
                res += val[j]*(capacity/wt[j])
                return res
        
        return res