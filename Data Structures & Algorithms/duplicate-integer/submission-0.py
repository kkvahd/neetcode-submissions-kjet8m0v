class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()
        for i in nums:
            if i in hash_map:
                return True
            hash_map.add(i)
        return False