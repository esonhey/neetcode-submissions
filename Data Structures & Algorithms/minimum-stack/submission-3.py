class MinStack:
    def __init__(self):
        self.val = { "min": None }

    def push(self, val: int) -> None:
        new_min = val if self.val["min"] == None else min(val, self.val["min"])
        self.val = {"v": val, "min": new_min, "i": self.val}

    def pop(self) -> None:
        self.val = self.val["i"]

    def top(self) -> int:
        return self.val["v"]

    def getMin(self) -> int:
        return self.val["min"]
