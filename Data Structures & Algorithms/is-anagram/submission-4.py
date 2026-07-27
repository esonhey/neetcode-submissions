class Solution:
    def countStr(self, s: str):
        counter = {}
        for c in s:
             counter[c] = counter.get(c, 0) + 1
        return counter

    def isAnagram(self, s: str, t: str) -> bool:
        countedS = self.countStr(s)
        countedT = self.countStr(t)

        return countedS == countedT