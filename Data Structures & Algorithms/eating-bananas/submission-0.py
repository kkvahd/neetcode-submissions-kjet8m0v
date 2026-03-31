class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, f = 1, max(piles)
        res = f

        while s <= f:
            curr = (s + f) // 2
            curr_t = 0
            
            for i in piles:
                curr_t += math.ceil(float(i) / curr)
            if curr_t <= h:
                res = curr
                f = curr - 1
            else:
                s = curr + 1
                    
        return res