from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True

        for i in range(len(s) + 1):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        return False

    def wordBreakDp(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
        return dp[0]


Solution().wordBreak("leetcode", ["leet", "code"])
