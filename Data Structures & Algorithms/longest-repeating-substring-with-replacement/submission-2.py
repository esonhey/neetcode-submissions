class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        act = s[0]
        rep = 0
        longest = 0
        hash_set = set([act])
        while r < len(s):
            curr = s[r]
            hash_set
            if act == curr:
                r += 1
            elif rep == k:
                if s[r-1] == s[r]:
                    r += 1
                    continue
                longest = max(longest, r - l)
                while l < len(s) and s[l] == act:
                    l += 1
                act = s[l]
                r = l + 1
                rep = 0
            else:
                print('____')
                rep += 1
                r += 1

        return max(longest, r - l)


            

