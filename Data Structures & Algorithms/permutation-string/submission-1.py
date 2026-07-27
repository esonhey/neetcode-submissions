class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = 0
        e = 0
        chars = s1
        while e < len(s2):
            if s2[e] in chars:
                chars = chars.replace(s2[e], '', 1)
                if len(chars) == 0: return True
                e += 1
            else:
                chars = s1
                s = s + 1
                e = s
        return False



        

        