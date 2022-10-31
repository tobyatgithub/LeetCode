# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # idea: mark all the depth, then bfs one time to find the answer -> N + N

        # 1. mark the height of each node
        def dfs(node):
            if not node:
                return 0
            if node.right or node.left:
                node.height = max(dfs(node.left), dfs(node.right)) + 1
            if not node.right and not node.left:
                node.height = 0
            # print(node, node.height)
            return node.height

        dfs(root)

        # 2. bfs and find the ans
        ret = [-1] * len(queries)
        cache = {}
        for num in queries:
            cache[num] = 0
        queue = [root]
        cur_level = 0
        while queue:
            tmp_queue = []
            # while queue:
            #     tmp_queue.append(queue.pop(0))
            tmp_values = [_.val for _ in tmp_queue]
            tmp_heights = [_.height for _ in tmp_queue]
            targets = list(set(tmp_values).intersection(queries))
            for target in targets:
                # queryId = queries.index(target)
                heightId = tmp_values.index(target)
                select = [_ for index, _ in enumerate(tmp_heights) if index != heightId]
                if select:
                    queryAns = max(select) + cur_level
                else:
                    queryAns = cur_level - 1
                # print(queryAns, cur_level)
                # ret[queryId] = queryAns
                cache[target] = queryAns

            cur_level += 1

            for node in tmp_queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # handle query duplicates
        for i in range(len(ret)):
            ret[i] = cache[queries[i]]
        return ret
