class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        finishable = set()
        not_finishable = set()

        def dfs(num, visited):
            if num in not_finishable:
                return False

            if num in visited:
                not_finishable.add(num)
                return False

            if num in finishable:
                return True
            
            visited.add(num)

            for pre in [x for x in prerequisites if x[0] == num]:
                if not dfs(pre[1], visited):
                    not_finishable.add(pre[1])
                    visited.discard(num)
                    return False
            visited.discard(num)
            finishable.add(num)
            return True
    
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True