    



    // 1. in order traverse of a tree function,
    // !! a function without return (change in place)
    // !! pass in a list as function parameter
    public void inOrder(TreeNode node, List<int> list){
        if (node != null)
        {
            inOrder(node.left, list);
            list.Add(node.val);
            inOrder(node.right, list);
        }
    }