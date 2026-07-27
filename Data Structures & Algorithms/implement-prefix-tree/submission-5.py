class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            curr[c] = curr.get(c, {})
            curr = curr[c]
            if i == len(word) - 1:
                curr["END"] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr:
                return False
            curr = curr.get(c)
            if i == len(word) - 1 and not curr.get("END", False):
                return False
        return True




    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, c in enumerate(prefix):
            if c not in curr:
                return False
            curr = curr.get(c)
        return True

        