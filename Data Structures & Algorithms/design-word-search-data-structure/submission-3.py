class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr[c] = curr.get(c, {})
            curr = curr[c]
        curr["END"] = True

    def search(self, word: str, curr_ = None) -> bool:
        curr = curr_ or self.root
        i = 0
        while i < len(word) and word[i] != '.':
            c = word[i]
            if c in curr:
                curr = curr[c]
                i += 1
                continue
            else:
                return False

        if i < len(word):
            for x in curr.keys():
                if x == 'END':
                    continue
                if self.search(word[i+1:], curr[x]):
                    return True
            return False
             
        else:
            return curr.get("END", False)
    
