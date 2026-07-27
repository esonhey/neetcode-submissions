class PrefixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr[c] = curr.get(c, {})
            curr = curr[c]
        curr["END"] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr.get(c)
        return curr.get("END", False)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr.get(c)
        return True

        