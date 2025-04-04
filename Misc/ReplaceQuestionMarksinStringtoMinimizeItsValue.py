import heapq

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = {}
        unknown_count = 0
        for ch in s:
            if ch != '?':
                freq[ch] = freq.get(ch, 0) + 1
            else:
                unknown_count += 1

        heap = [(freq.get(ch, 0), ch) for ch in 'abcdefghijklmnopqrstuvwxyz']
        heapq.heapify(heap)
        
        # So that we can put the characters in the least frequently occured manner with least lexicographical order 
        replacements = []
        for _ in range(unknown_count):
            count, ch = heapq.heappop(heap)
            replacements.append(ch)
            heapq.heappush(heap, (count + 1, ch))
        
        replacements.sort()

        # We start making the new string
        res = []
        i = 0
        for ch in s:
            if ch == '?':
                res.append(replacements[i])
                i += 1
            else:
                res.append(ch)

        return ''.join(res)
