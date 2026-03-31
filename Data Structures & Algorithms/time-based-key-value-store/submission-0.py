class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [[value, timestamp]]
        else:
            self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        nums = self.time_map[key]
        if nums[0][1] > timestamp:
            return ""

        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            curr = nums[m][1]
            
            if curr > timestamp:
                r = m - 1
            elif curr < timestamp:
                res = m
                l = m + 1
            else:
                res = m
                break
        return nums[res][0] if res > -1 else ""
