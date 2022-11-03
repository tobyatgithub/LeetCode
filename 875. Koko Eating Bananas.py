from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    def findTimeNeeded(piles: List[int], speed: int) -> int:
        if speed == 0:
            return math.inf
        ret = 0
        for pile in piles:
            ret += math.ceil(pile / speed)
        return ret

    l, r = 1, max(piles)  # speed in banana per hour
    while l < r:  # find the minimum such that time needed < h
        m = l + (r - l) // 2
        time = findTimeNeeded(piles, m)  # searching the lower upper bound
        if time <= h:
            r = m
        else:
            l = m + 1
    print(l)
    return l
    # m = l + (r - l) // 2
    # time = findTimeNeeded(piles, m)  # searching the lower upper bound
    # if time <= h:
    #     r = m
    # else:
    #     l = m + 1

    # return False


minEatingSpeed([1, 1, 1, 999999999], 10)  # 142857143
minEatingSpeed([30, 11, 23, 4, 20], 5)  # 30
minEatingSpeed([312884470], 312884469)  # 2
