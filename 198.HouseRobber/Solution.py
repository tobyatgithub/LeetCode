class Solution:

    def recurssive_rob(self, i, nums):
        if i < 0:
            return 0
        if i not in self.cache:
            self.cache[i] = max(self.recurssive_rob(i-1,nums), self.recurssive_rob(i-2, nums) + nums[i])
        return self.cache[i]

    
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        return self.recurssive_rob(len(nums)-1, nums)