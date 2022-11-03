class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs_lowerBound(nums, target):  # return index
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            # print(l)
            return l

        def bs_upperBound(nums, target):  # not inclusive [l, r)
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            # print(l, r)
            return l

        # search to see find
        upper = bs_upperBound(nums, target) - 1
        lower = bs_lowerBound(nums, target)
        if lower == len(nums):
            return [-1, -1]
        if nums[lower] != target:
            return [-1, -1]
        return [lower, upper]


def bs_lowerBound(nums, target):  # return index
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if nums[m] >= target:
            r = m
        else:
            l = m + 1
    print(l)
    return l


def bs_upperBound(nums, target):  # not inclusive [l, r)
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > target:
            r = m
        else:
            l = m + 1
    print(l, r)
    return l


# test
a = [5, 7, 7, 8, 8, 10]
bs_lowerBound(a, 10)
bs_lowerBound(a, 8)
bs_lowerBound([5], 5)
bs_lowerBound(a, 6)

bs_upperBound(a, 10)
bs_upperBound(a, 8)
bs_upperBound([5], 5)
bs_upperBound(a, 6)
