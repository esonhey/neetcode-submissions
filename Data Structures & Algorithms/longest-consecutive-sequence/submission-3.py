def find_indexes(fn, lst):
    idxs = []
    for i in range(0, len(lst)):
        if fn(lst[i]):
            idxs.append(i)
    return idxs

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        groups = []
        for x in nums:
            idxs = find_indexes(lambda set_item: (x in set_item) or (x-1 in set_item) or (x+1 in set_item), groups)
            if (len(idxs) == 1):
                groups[idxs[0]].add(x)
            elif (len(idxs) == 2):
                groups[idxs[0]].add(x)
                groups[idxs[0]] = groups[idxs[0]].union(groups[idxs[1]])
                groups = groups[:idxs[1]] + groups[idxs[1]+1:]
            elif len(idxs) == 0:
                groups.append(set([x]))
        
        group_sizes = map(lambda x: len(x),groups)
        return max(*group_sizes,0,0)