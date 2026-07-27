from itertools import product
class Solution:
    digitMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi", 
        "5": "jkl", 
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv", 
        "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return [''.join(x) for x in product(*[self.digitMap[d] for d in digits])]
    
        