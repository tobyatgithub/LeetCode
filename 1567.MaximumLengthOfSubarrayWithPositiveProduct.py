def getMaxLength(nums):
    for i in range(len(nums)):
        print(nums[i])
        i += 1


# def getMaxLength(nums):
#     pos, neg, ans = 0, 0, 0
#     for n in nums:
#         new_pos, new_neg = 0, 0
#         if n > 0:
#             new_pos = pos + 1
#             new_neg = neg + 1 if neg > 0 else 0
#         elif n < 0:
#             new_pos = neg + 1 if neg > 0 else 0
#             new_neg = pos + 1

#         pos, neg = new_pos, new_neg
#         ans = max(ans, pos)
#     print(ans)
#     return ans


getMaxLength([1, -2, -3, 4, 0, 5, -6, -7, 8, 9])
