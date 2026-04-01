class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            print(m)
            curr = 0
            
            for i in piles:
                curr += math.ceil(float(i) / m)

            if curr > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)

        return res