# class Solution:
#     # 1 - need to fix the cache.
#     # 2 - lru_cache decorator can only be used on hashable objects (i.e. can't be applied on dict)
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         def isValid(word, lookup):
#             #             print(f"word = {word}")
#             #             print("cache = ", cache)
#             #             print()

#             #             if word in cache:
#             #                 return cache[word]
#             if word in res:
#                 return True

#             if len(word) == 0:
#                 return True
#             first_letter = word[0]
#             for candidate in lookup[first_letter]:
#                 if candidate == word[: len(candidate)] and isValid(
#                     word[len(candidate) :], lookup
#                 ):
#                     cache[word] = True
#                     return True
#             # cache[word] = False
#             return False

#         cache = {}
#         from collections import defaultdict

#         lookup = defaultdict(set)
#         # form
#         for word in words:
#             if len(word) == 0:
#                 continue
#             lookup[word[0]].add(word)  # key: first letter, value: word

#         res = []
#         for word in words:
#             if len(word) == 0:
#                 continue
#             lookup[word[0]].remove(word)
#             if isValid(word, lookup):
#                 res.append(word)
#             lookup[word[0]].add(word)
#         return res


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        cache = {}
        from collections import defaultdict

        lookup = defaultdict(set)

        # form
        for word in words:
            if len(word) == 0:
                continue

            if word[0] not in lookup:
                lookup[word[0]] = set()
            lookup[word[0]].add(word)  # key: first letter, value: word

        def isValid(word, lookup):
            nonlocal cache
            if word in cache:
                return cache[word]

            if len(word) == 0:
                return True
            first_letter = word[0]
            for candidate in lookup[first_letter]:
                if candidate == word[: len(candidate)] and isValid(
                    word[len(candidate) :], lookup
                ):
                    cache[word] = True
                    return True
            return False

        res = []
        for word in words:
            if len(word) == 0:
                continue
            lookup[word[0]].remove(word)
            if isValid(word, lookup):
                res.append(word)
            print(f"word = {word}")
            print("res = ", res)
            print("cache = ", cache)
            print()

            lookup[word[0]].add(word)

        return res
