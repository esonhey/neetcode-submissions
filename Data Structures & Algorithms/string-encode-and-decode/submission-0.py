class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = 0
            while s[i] != '#': 
                count = count*10 + int(s[i])
                i += 1
            i += count + 1
            res.append(s[i-count:i]) 
        return res

