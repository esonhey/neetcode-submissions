class PrefixTree:

    def __init__(self):
        self.v = set()
        self.p = set()

    def insert(self, word: str) -> None:
        self.v.add(word)
        for i in range(1, len(word)):
            self.p.add(word[0:i])

    def search(self, word: str) -> bool:
        return word in self.v

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.v or prefix in self.p

        