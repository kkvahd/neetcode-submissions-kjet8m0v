class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        heapq.heapify(heap)

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        for i in freq:
            heapq.heappush(heap, (freq[i], i))

            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]

        


