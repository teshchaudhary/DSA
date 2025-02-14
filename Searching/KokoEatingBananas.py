class Solution:
    def currentSpeed(self, piles, mid, h):
        res = 0
        for pile in piles:
            res += pile // mid
            if pile % mid != 0:
                res += 1
            
        return res <= h  # Return True if within the hours, otherwise False

    def minEatingSpeed(self, piles, h) -> int:
        si = 1  # Start speed
        ei = max(piles)  # Maximum speed is the size of the largest pile

        while si < ei:
            mid = (si + ei) // 2
            if self.currentSpeed(piles, mid, h):  # Check if speed mid is valid
                ei = mid  # Try for a smaller speed
            else:
                si = mid + 1  # Increase the speed

        return si  # This will be the minimum speed found