'''Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).'''
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ctr = []
        path = []
        def dfs(i):
            path.append(i)                                   # Add current node to path
            print(f'i = {i} path = {path} ctr = {ctr}')      # remove this while running on leetcode else it'll show OUTPUT LIMIT REACHED ERROR
            if i == len(graph)-1:                            # If we reached the target node
                ctr.append(path[:])                          # Append a copy of the path
            else:
                for j in graph[i]:                           # Explore all possible next nodes
                    dfs(j)
            path.pop()                                       # Backtrack to explore other paths
        dfs(0)                                               # Start DFS from node 0
        return ctr

mySol = Solution()
graph = [[1,2],[3],[3],[]]
print(mySol.allPathsSourceTarget(graph))