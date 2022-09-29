// Merhod 1: Brutal Force
public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int[] aaa = new int[nums.Length];
        
        for (int i = 0; i < nums.Length; i++)
        {
            int tmp_count = 0;
            foreach (int val in nums.ToList().FindAll(e=>(e < nums[i])).ToList())
            {
                tmp_count += 1;
            }
            aaa[i] = tmp_count;
        }
        return aaa;
    }
}

// Method 2: sort and use a cache
public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int[] aaa = new int[nums.Length];
        Array.Copy(nums, 0, aaa, 0, nums.Length);
        Array.Sort(aaa);
        
        Dictionary <int, int> store = new Dictionary <int, int>();
        for (int i = 0; i < aaa.Length; i++)
        {
            if (store.ContainsKey(aaa[i]) == false)
            {
                store[aaa[i]] = i;
            }
        }
        
        for (int i = 0; i < nums.Length; i++)
        {
            aaa[i] = store[nums[i]];
        }
        return aaa;
    }
}