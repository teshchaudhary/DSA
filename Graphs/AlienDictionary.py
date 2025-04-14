#User function Template for python3
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
            
        return "".join(order)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
from collections import deque

#Position this line where user code will be pasted.


def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends