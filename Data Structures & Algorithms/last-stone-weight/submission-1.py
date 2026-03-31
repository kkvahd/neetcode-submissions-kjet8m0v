class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one = abs(heapq.heappop(stones))
            two = max(abs(heapq.heappop(stones)), 0)
            print(one)
            print(two)

           
            heapq.heappush(stones, -(one - two))

        return abs(stones[0])