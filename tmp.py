# import math

# N = 1000
# table = [None for _ in range(N + 2)]  # p_i (0)
# table[2], table[3] = 1, 2
# index = 4

# while index <= N:
#     table[index] = (index - 1) * (table[index - 1] + table[index - 2])
#     index += 1

# print(table[N] / math.factorial(N))

# def bubble_sort(a):
#     for i in range(n, 0, -1):  # i = n, n - 1, ..., 1
#         for j in range(1, i):  # j = 1, 2, ..., i - 1
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]  # swap
#     return a


# # def rec(n):
# #     if n == 2:
# #         return 2
# #     return 2 * rec(n // 2) + n


# # print(rec(2048))


# total = 0
# for i in range(1, 12):
#     top = i * 2 ** (i - 1)
#     total += top
#     print(f"i = {i}, top = {top}, total = {total}")


array = [4, 6, 10, 8, 2, 1]
m = 3

start = 0
end = m

maxSum = sum(array[start:end])
print("maxSum = ", maxSum)
cur = maxSum

while end < len(array) - 1:
    cur -= array[start]
    start += 1
    cur += array[end]
    end += 1
    maxSum = max(maxSum, cur)
    print("maxSum = ", maxSum)

result = sum(array) - maxSum

print(result)
