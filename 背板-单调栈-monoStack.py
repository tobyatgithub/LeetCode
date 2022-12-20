"""
monotonic stack is a super useful tool in many code challenges,
such as 84. Largest Rectangle in Histogram, 1950.Maximum-of-Minimum-Values-in-All-Subarrays, etc.
find more in https://github.com/wisdompeak/LeetCode (and search for monotonic stack key word)

Here is one basic way of realizing it.
"""
heights = []  # input list

n = len(heights)

stack = []
nextSmaller = [n] * n
for i in range(n):
    while stack and height[stack[-1]] > height[i]:
        nextSmaller[stack.pop(-1)] = i
    stack.append(i)

stack = []
prevSmaller = [-1] * n
for i in range(n, -1, -1):
    while stack and height[stack[-1]] > height[i]:
        prevSmaller[stack.pop(-1)] = i
    stack.append(i)

# for example in the 84. histogram area question
ret = 0
for i in range(n):
    area = heights[i] * (nextSmaller[i] - prevSmaller[i] - 1)
    ret = max(ret, area)
return ret
