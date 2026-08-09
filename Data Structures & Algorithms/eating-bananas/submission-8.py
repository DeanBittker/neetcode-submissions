class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        L = 1
        R = max(piles)
        while L <= R:
            k = (L + R)//2
            total_hours = 0
            for item in piles:
                total_hours += ((item//k) + 1 if item % k > 0 else item//k)
            if total_hours > h:
                L = k+1
            elif total_hours <= h:
                R = k-1
        return L
        


