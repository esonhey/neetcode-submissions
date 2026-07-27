class Solution:
    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        self.dfs(0, s, part, res);
        return res
    
    def dfs(self, i, s, part, res):
        if (i >= len(s)):
            res.append([*part])
            return
        for j in range(i, len(s)):
            if self.isPal(s, i, j):
                part.append(s[i:j+1])
                self.dfs(j+1, s, part, res);
                part.pop()
            



        