class MinStack:

    def __init__(self):
        self.linked_stack = None

    def push(self, val: int) -> None:
        new_min = val if self.linked_stack == None else min(self.linked_stack["min_val"], val)
        self.linked_stack = { "value": val, "min_val": new_min, "next": self.linked_stack }

    def pop(self) -> None:
        self.linked_stack = self.linked_stack["next"]
        

    def top(self) -> int:
        return self.linked_stack["value"]

    def getMin(self) -> int:
        return self.linked_stack["min_val"]

        
