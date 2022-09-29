class Solution:
    def find_all_ones(self, grid):
        # given a list of list of int, return the locations where 
        # element == 1
        tmp_out = []
        if grid:
            for i in range(len(grid[0])):
                for j in range(len(grid)):
                    if grid[i][j] == 1:
                        tmp_out.append((i,j))
        return tmp_out

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        onesA = self.find_all_ones(A)
        onesB = self.find_all_ones(B)
        cache = defaultdict(int)
        max_count = 0
        
        for (x_a, y_a) in onesA:
            for (x_b, y_b) in onesB:
                vector = (x_b - x_a, y_b - y_a)
                cache[vector] += 1
                max_count = max(max_count, cache[vector])
                # print(x_a, y_a, x_b, y_b)
                # break
        return max_count
                
            