class Solution:
    def deleteString(self, s: str) -> int:
        if all(x == s[0] for x in s):
            return len(s)

        @cache
        def dfs(word_index):
            length = len(s) - word_index
            if length == 1:
                return 1
            res = 1
            for i in range(1, length // 2 + 1):
                if len(s) - word_index - i + 1 <= res:
                    break
                if (
                    s[word_index : word_index + i]
                    == s[word_index + i : word_index + 2 * i]
                ):
                    res = max(res, 1 + dfs(word_index + i))
            return res

        res = dfs(0)
        return res
