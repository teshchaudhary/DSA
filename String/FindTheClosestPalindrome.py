class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        # Special cases

        # 1-9
        if num <= 10:
            return str(num - 1)
        
        # Edge case
        if n == "11":
            return "9"
        
        # like 100, 1000, etc. -> 99, 999
        if set(n[1:]) == {'0'} and n[0] == '1':  
            return str(num - 1)
        
        # like 9, 99, 999, etc. -> 11, 101, 1001
        if set(n) == {'9'}:  
            return str(num + 2)
        

        prefix = int(n[:(length + 1) // 2])

        # We add 5 types of things in the candidates
        # handled for both even and odd length cases
        #   -> 1. Mirror of prefix as-is (same middle)
        #   -> 2. Mirror of (prefix - 1)
        #   -> 3. Mirror of (prefix + 1)
        #   -> 4. 10^(length - 1) - 1  (e.g., 999 for 1001)  [lower bound]
        #   -> 5. 10^length + 1       (e.g., 10001 for 9999) [upper bound]


        candidates = set()
        
        for diff in [-1, 0, 1]:
            new_prefix = str(prefix + diff)
            if length % 2 == 0:
                pal = new_prefix + new_prefix[::-1]
            else:
                pal = new_prefix + new_prefix[:-1][::-1]
            candidates.add(pal)
        
        candidates.add(str(10 ** (length - 1) - 1))
        candidates.add(str(10 ** length + 1))
        
        candidates.discard(n)  # Exclude original number
        closest = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
        return closest
