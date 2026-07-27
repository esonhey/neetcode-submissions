class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        res = 0
        l, r = 0,0
        while r < len(s):
            curr = s[r] 
            if curr not in ss:
                ss.add(curr)
                res = max(res, len(ss))
            else:
                while s[l] != curr:
                    ss.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return res

        