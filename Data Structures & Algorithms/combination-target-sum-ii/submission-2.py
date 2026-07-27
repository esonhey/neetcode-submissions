class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(collected, remaining, tar):
            for i in range(len(remaining)):
                t = remaining[i]
                if t > tar or (remaining[i - 1] == remaining[i] and i>0):
                    continue
                newCollected = sorted(collected + [t])
                if t == tar:
                    result.append(newCollected)
                print(remaining, tar)
                print(newCollected, target)
                dfs(newCollected, remaining[i+1:], tar - t)

        dfs([], candidates, target)
        return result

        

        