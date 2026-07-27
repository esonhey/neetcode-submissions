from itertools import product
class Solution:
    digitMap = ["+", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def letterCombinations(self, digits: str) -> List[str]:
        maped = [self.digitMap[int(d)] for d in digits]
        if not maped:
            return maped
        return [''.join(x) for x in product(*maped)]
    
        