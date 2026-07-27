class TimeMap:

    def __init__(self):
        self.last = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.last[key] = self.last.get(key, [])
        self.last[key].append({"value": value, "timestamp": timestamp})

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.last:
            return ""
        
        curr = self.last.get(key)
        print("curr", curr)
        l, r = 0, len(curr) - 1
        for i in range(len(curr) -1, -1, -1):
            if timestamp >= curr[i]["timestamp"]:
                return curr[i]["value"]
        return ""

        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if timestamp < curr[l]["timestamp"]:
        #         if timestamp >= curr[l-1]["timestamp"]:
        #             return curr[l-1]["value"]
        #         return ""
        #     if (curr[mid]["timestamp"] <= timestamp):
        #         l = mid + 1
        #     else:
        #         r = mid - 1

        
