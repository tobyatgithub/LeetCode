import math
from typing import List


#failed
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dfs with early stop (k)
        # build graph
        adj = {i: [] for i in range(n)}
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))

        ret = math.inf
        cache = {}
        path = []
        
        def dfs(node, priceSoFar, stepSoFar, pathSoFar):
            nonlocal path
            if node == dst and stepSoFar <= k:
                path.append((priceSoFar, pathSoFar))
                return priceSoFar
            if stepSoFar > k:
                return math.inf
            if (node, stepSoFar) in cache:
                # print(node, stepSoFar, cache[(node, stepSoFar)])
                return cache[(node, stepSoFar)]

            ans = math.inf
            for to_i, price_i in adj[node]:
                ans = min(ans, dfs(to_i, priceSoFar+price_i, stepSoFar+1, pathSoFar + "-" + str(to_i)))
            cache[(node, stepSoFar)] = ans
            # print(path)
            return ans

        ret = dfs(src, 0, -1, str(src))
        print(path)
        return ret if ret != math.inf else -1




print("solution1")
testFLights = [[10, 14, 43], [1, 12, 62], [4, 2, 62], [14, 10, 49], [9, 5, 29], [13, 7, 53], [4, 12, 90], [14, 9, 38], [11, 2, 64], [2, 13, 92], [11, 5, 42], [10, 1, 89], [14, 0, 32], [9, 4, 81], [3, 6, 97], [7, 13, 35], [11, 9, 63], [5, 7, 82], [13, 6, 57], [4, 5, 100], [2, 9, 34], [11, 13, 1], [14, 8, 1], [12, 10, 42], [2, 4, 41], [0, 6, 55], [
    5, 12, 1], [13, 3, 67], [3, 13, 36], [3, 12, 73], [7, 5, 72], [5, 6, 100], [7, 6, 52], [4, 7, 43], [6, 3, 67], [3, 1, 66], [8, 12, 30], [8, 3, 42], [9, 3, 57], [12, 6, 31], [2, 7, 10], [14, 4, 91], [2, 3, 29], [8, 9, 29], [2, 11, 65], [3, 8, 49], [6, 14, 22], [4, 6, 38], [13, 0, 78], [1, 10, 97], [8, 14, 40], [7, 9, 3], [14, 6, 4], [4, 8, 75], [1, 6, 56]]
Solution().findCheapestPrice(n=15, flights=testFLights, src=1, dst=4, k=10) # expected: 169


#case 1
# testFLights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# Solution().findCheapestPrice(n=4, flights=testFLights, src=0, dst=3, k=1) # expected: 700
# print()
# Solution().findCheapestPrice(n=4, flights=testFLights, src=0, dst=3, k=2) # expected: 400

# passed
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dfs with early stop (k)
        # build graph
        adj = {i: [] for i in range(n)}
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))

        ret = math.inf
        cache = {}
        path = []
        def dfs(node, priceSoFar, stepSoFar, pathSoFar):
            nonlocal path
            if node == dst and stepSoFar <= k:
                path.append((priceSoFar, pathSoFar))
                return 0
            if stepSoFar > k:
                return math.inf
            if (node, stepSoFar) in cache:
                # print(node, stepSoFar, cache[(node, stepSoFar)])
                return cache[(node, stepSoFar)][0]

            ans = math.inf
            for to_i, price_i in adj[node]:
                # ans = min(ans, dfs(to_i, priceSoFar+price_i, stepSoFar+1))
                ans = dfs(to_i, priceSoFar, stepSoFar+1, pathSoFar + "-" + str(to_i)) + price_i

            cache[(node, stepSoFar)] = [ans, pathSoFar+"-"+str(to_i)]
                    # print(cache)
            # print(path)
            return ans

        ret = dfs(src, 0, -1, str(src))
        print(path)
        return ret if ret != math.inf else -1

print("solution2")
testFLights = [[10, 14, 43], [1, 12, 62], [4, 2, 62], [14, 10, 49], [9, 5, 29], [13, 7, 53], [4, 12, 90], [14, 9, 38], [11, 2, 64], [2, 13, 92], [11, 5, 42], [10, 1, 89], [14, 0, 32], [9, 4, 81], [3, 6, 97], [7, 13, 35], [11, 9, 63], [5, 7, 82], [13, 6, 57], [4, 5, 100], [2, 9, 34], [11, 13, 1], [14, 8, 1], [12, 10, 42], [2, 4, 41], [0, 6, 55], [
    5, 12, 1], [13, 3, 67], [3, 13, 36], [3, 12, 73], [7, 5, 72], [5, 6, 100], [7, 6, 52], [4, 7, 43], [6, 3, 67], [3, 1, 66], [8, 12, 30], [8, 3, 42], [9, 3, 57], [12, 6, 31], [2, 7, 10], [14, 4, 91], [2, 3, 29], [8, 9, 29], [2, 11, 65], [3, 8, 49], [6, 14, 22], [4, 6, 38], [13, 0, 78], [1, 10, 97], [8, 14, 40], [7, 9, 3], [14, 6, 4], [4, 8, 75], [1, 6, 56]]
Solution().findCheapestPrice(n=15, flights=testFLights, src=1, dst=4, k=10) # expected: 169

print()

# visualization
import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

for source, destination, weight in testFLights:
    G.add_edge(str(source), str(destination), weight=weight)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=1)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=4, arrowstyle="->", arrowsize=10)
nx.draw_networkx_edges(G, pos, node_size=300, width=4, arrowstyle="->", arrowsize=10)
# nx.draw_networkx_edges(
#     G, pos, edgelist=esmall, width=4, alpha=0.5, edge_color="b", style="dashed"
# )
# edges = nx.draw_networkx_edges(
#     G,
#     pos,
#     node_size=node_sizes,
#     arrowstyle="->",
#     arrowsize=10,
#     edge_color=edge_colors,
#     edge_cmap=cmap,
#     width=2,
# )


# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()