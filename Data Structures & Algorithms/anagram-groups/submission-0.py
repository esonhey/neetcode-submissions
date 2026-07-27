class Solution:
    def toAnagram (self, string: str) -> str:
        count = {}
        for c in string:
            count[c] = count.get(c, 0) + 1
        return ''.join(sorted(map(lambda x: x[0]+str(x[1]),count.items())))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for string in strs:
             anagram = self.toAnagram(string)
             grouped[anagram] = grouped.get(anagram, []) + [string]

        return grouped.values()
        