class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        head, end = newInterval
        output = []
        
        while i < len(intervals):
            cur_head, cur_end = intervals[i]
            # we only need to insert one interval
            # and the first task is to find where to start
            if head <= cur_end:
                if end < cur_head:
                    # easy case, new interval shall be at position 0
                    break
                else:
                    # start merging, we will keep doing this
                    # until the updated end < cur_head
                    head = min(head, cur_head)
                    end = max(end, cur_end)
            # merge not start yet, append
            else:
                output.append(intervals[i])
            i += 1
        output.append([head,end])
        output.extend(intervals[i:])
        return output
            
            
            