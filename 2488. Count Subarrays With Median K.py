from typing import List
import collections


def countSubarrays(nums: List[int], k: int) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] < k:
            nums[i] = -1
        elif nums[i] == k:
            nums[i] = 0
        else:
            nums[i] = 1

    ret = 0
    presum_odd = collections.defaultdict(int)
    presum_even = collections.defaultdict(int)
    # presum_even[0] = 1
    presum_odd[0] = 1

    curPresum = 0
    for i in range(n):
        curPresum += nums[i]
        if i % 2 == 0:  # nums[0:i] is even length
            ret += presum_odd[curPresum - 0]
            ret += presum_even[curPresum - 1]
            presum_even[curPresum] += 1
        else:
            ret += presum_odd[curPresum - 1]
            ret += presum_even[curPresum - 0]
            presum_odd[curPresum] += 1
    return ret
    # n = len(nums)

    # for i in range(n):
    #     if nums[i] > k:
    #         nums[i] = 1
    #     elif nums[i] == k:
    #         nums[i] = 0
    #     else:
    #         nums[i] = -1

    # ret = 0
    # presum_even = collections.defaultdict(int)
    # presum_odd = collections.defaultdict(int)

    # presum_even[0] = 1
    # s = 0  # s是前缀和
    # for i in range(n):
    #     s += nums[i]
    #     if i % 2 == 0:
    #         ret += presum_even[
    #             s - 0
    #         ]  # 寻找之前所有 长度为偶数 并且前缀和是s的项目，找到的话 nums[that+1:i]的和就是0！
    #         ret += presum_odd[s - 1]
    #         presum_odd[s] += 1
    #     else:
    #         ret += presum_even[s - 1]
    #         ret += presum_odd[s - 0]
    #         presum_even[s] += 1
    # return ret


k = 4
case1 = [3, 2, 1, 4, 5]
case2 = [2, 3, 1, 2, 3, 1, 5, 2, 4, 4, 10, 2, 3, 1, 11, 22, 1, 9]
case3 = [2, 5, 1, 4, 3, 6]
case4 = [4, 1, 3, 2]

# countSubarrays(case1, k)
countSubarrays(case4, 1)

