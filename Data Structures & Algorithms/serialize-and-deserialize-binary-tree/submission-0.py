# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class LinkedList:
    def __init__(self, val=0, child=None):
        self.val = val
        self.child = child

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        def dfs(root):
            serialized.append(root.val if root is not None else "N")
            # if root is None:
            #     serilized.append(None)
            #     return
            # serialized.append(root.val)
            if root is not None:
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        value = ",".join([str(num) for num in serialized]) 
        print(value)
        return value

            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None

        arr = data.split(",")
        self.i = 0

        def dfs():
            if arr[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(arr[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
