class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        i = 0
        res = []

        while i < len(sortedNums):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                i += 1
                continue
            qualifiedPairs = self.twoSum(sortedNums[i + 1 :], sortedNums[i])
            if qualifiedPairs:
                print(qualifiedPairs)
                res.extend(qualifiedPairs)
            i += 1

        return res

    def twoSum(self, sortedNums, target):
        l, r = 0, len(sortedNums) - 1
        res = []
        while l < r:
            numL = sortedNums[l]
            numR = sortedNums[r]
            if numL + numR == -target:
                toAdd = [numL, numR, target]
                if toAdd not in res:
                    res.append(toAdd)
                l += 1
                # r -= 1
            if numL + numR < target:
                l += 1
            if numL + numR > target:
                r -= 1
        return res
