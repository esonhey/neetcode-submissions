class Solution:
    def stringHash(self, s: str):
        hashMap = {}
        for c in s:
            hashMap[c] = 1 + hashMap.get(c, 0)
        return hashMap

    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, -1
        tHash = self.stringHash(t)
        wHash = {}
        tv = len(tHash.keys())
        wv = 0

        result = None

        while r < len(s):
            if wv < tv:
                r += 1
                if r == len(s):
                    break
                if s[r] in tHash:
                    wHash[s[r]] = wHash[s[r]] + 1 if s[r] in wHash else 1

                    if wHash[s[r]] == tHash[s[r]]:
                        wv += 1

                    if wv == tv:
                        if result is None or r-l < len(result):
                            result = s[l:r+1]
            
            else:
                # ✅ Capture while window is still guaranteed valid
                if r - l + 1 < len(result):
                    result = s[l:r+1]

                if s[l] in wHash:
                    wHash[s[l]] -= 1
                    if wHash[s[l]] < tHash[s[l]]:
                        wv -= 1

                l += 1

        return result if result != None else ""

        