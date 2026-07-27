class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sortedHand = sorted(hand)
        print(sortedHand)

        def removeInitialSort(sortedList: List[int], expected, idx, remaining) -> bool:
            if remaining == 0:
                return True

            initVal = sortedList[idx]
            if initVal != expected: return False

            del sortedList[idx]
            nextIdx = idx

            if remaining == 1:
                return True

            while nextIdx < len(sortedList) and sortedList[nextIdx] == initVal:
                nextIdx += 1

            if nextIdx == len(sortedList):
                return False

            return removeInitialSort(sortedList, initVal +1, nextIdx, remaining - 1)
            
        def isStraight(sortedHand: List[int]) -> bool:
            print('sortedHand', sortedHand)
            if not len(sortedHand):
                return True

            foundSort = removeInitialSort(sortedHand, sortedHand[0], 0, groupSize)
            print('after remove', sortedHand, foundSort)
            if foundSort:
                return isStraight(sortedHand)

            return False

        return isStraight(sortedHand)