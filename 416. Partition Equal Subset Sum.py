from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        ## Let's look into way we can not use list and need set
        ## It turns out that:
        ## using for seenValue in dp will result an unexpected extended for loop
        ## such that each iteration we add a new value to it and it keeps running.
        ## What's more, using list instead of set will lead to a memory limit exceed 
        ## on leetcode
        # dp = [0]
        # for i, num in enumerate(nums):
        #     # for seenValue in dp:
        #     for j in range(len(dp)):
        #         seenValue = dp[j]
        #         if seenValue + num == target:
        #             return True
        #         dp.append(seenValue + num)
        # return False

        # Correct way: using set
        dp = set()
        dp.add(0)
        # for i in range(len(nums)):
        for num in nums:
            nextDP = set()
            for seenValue in dp:
                if seenValue + num == target:
                    return True
                nextDP.add(seenValue + num)
                nextDP.add(seenValue)
            dp = nextDP
        return False


case1 = [3, 3, 3, 4, 5]  # true
case2 = [1, 2, 5]  # false
result = Solution().canPartition(case2)
print(result)
