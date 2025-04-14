from collections import defaultdict, deque

class Solution:

    def findOrder(words):
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch] = []
                if ch not in indegrees:
                    indegrees[ch] = 0
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    indegrees[word2[j]] += 1
                    break
        
        q = deque([ch for ch in indegrees if indegrees[ch] == 0])
        order = []
        
        while q:
            ch = q.popleft()
            order.append(ch)
            for neighbor in adj[ch]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        if len(order) != len(indegrees):
            return ""
            
        return order