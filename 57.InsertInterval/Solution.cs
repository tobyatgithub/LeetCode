public class Solution {
    // Notice this is not the best practical solution
    // Shall come back later for better coding
    // e.g. use linkedlist
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        int head = newInterval[0];
        int end = newInterval[1];
        List<int[]> output = new List<int[]>();
        
        int i = 0;
        while (i < intervals.Count())
        {
            int cur_head = intervals[i][0], cur_end = intervals[i][1];
            if (head <= cur_end)
            {
                if (end < cur_head)
                {
                    break;
                }
                else
                {
                    head = Math.Min(head, cur_head);
                    end = Math.Max(end, cur_end);
                }
            }
            else
            {
                output.Add(intervals[i]);
            }
            i += 1;
        }
        output.Add(new int[2] {head, end});
        
        while (i < intervals.Count())
        {
            output.Add(intervals[i]);
            i++;
        }
        return output.ToArray();
    }
}