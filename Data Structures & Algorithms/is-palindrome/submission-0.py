import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  re.sub(r'\W', '', s).lower()
        for i in range(0, int(len(s) / 2)):
            if (s[i] != s[-(i + 1)]):
                return False
        return True
