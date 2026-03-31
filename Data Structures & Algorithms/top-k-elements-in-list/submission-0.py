class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        freq_arr = [[] for i in range(len(nums)+1)]
        res = []

        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1

        for i in freq_dict:
            f = freq_dict[i]
            freq_arr[f].append(i)

        for i in range(len(freq_arr)-1, 0, -1):
            if k == 0:
                break
            if len(freq_arr[i]) > 0:
                arr = freq_arr[i]
                for j in arr:
                    if k == 0:
                        break
                    res.append(j)
                    k -= 1
        return res
