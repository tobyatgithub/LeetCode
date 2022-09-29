public class Solution {
    public int MaxProduct(int[] nums) 
    {
        if (nums.Length == 0){
            return 0;
        }
        List<int> max_so_far = new List<int>() {nums[0]};
        List<int> min_so_far = new List<int>() {nums[0]};
        
        int maximum = nums[0];
        
        for (int i = 1; i < nums.Length; i++)
        {
            int n = nums[i];
            // Console.WriteLine("i = {0}, n = {1}", i, n);
            int local_max = new [] {n, n*max_so_far[i-1], n*min_so_far[i-1]}.Max();
            int local_min = new [] {n, n*max_so_far[i-1], n*min_so_far[i-1]}.Min();
            
            max_so_far.Add(local_max);
            min_so_far.Add(local_min);
            
            if (local_max > maximum)
            {
                maximum = local_max;
            }
        }
        
        
        return maximum;
    }
}