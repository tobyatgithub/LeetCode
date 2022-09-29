/**
2020-09-07 TAKE AWAY:
Queue doesn't support index;
List kind of doesn't support pop, but there's a way to hack it 
(get value and then RemoveAt(0))

public void for functions without a return (in place change)
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public List<int> list1 = new List<int>();
    public List<int> list2 = new List<int>();
    // public Queue<int> list1 = new Queue<int>();
    // public Queue<int> list2 = new Queue<int>();
    public List<int> output = new List<int>();
    
    public void inOrder(TreeNode node, List<int> list){
        if (node != null)
        {
            inOrder(node.left, list);
            list.Add(node.val);
            inOrder(node.right, list);
        }
    }
    
    public IList<int> GetAllElements(TreeNode root1, TreeNode root2) {
        inOrder(root1, list1);
        inOrder(root2, list2);
        
        while (list1.Count > 0 && list2.Count > 0)
        {
            if (list1[0] < list2[0])
            {
                output.Add(list1[0]);
                list1.RemoveAt(0);
            }
            else
            {
                output.Add(list2[0]);
                list2.RemoveAt(0);
            }
        }
        
        while (list1.Count > 0)
        {
            output.Add(list1[0]);
            list1.RemoveAt(0);
        }
        while (list2.Count > 0)
        {
            output.Add(list2[0]);
            list2.RemoveAt(0);
        }

        return output;
            
    }
}