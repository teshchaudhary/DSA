def maximumProfit(prices):
    n = len(prices)
    mini = prices[0]
    res = 0
    
    for i in range(1, n):
        curr = prices[i]
        res = max(res, curr - mini)
        mini = min(curr, mini)
    
    return res