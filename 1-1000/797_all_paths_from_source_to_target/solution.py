graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [],
}


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # graph = {i: neighbors for i, neighbors in enumerate(graph)}
        paths = []

        def dfs(graph, start, end, path):
            if start == end:
                paths.append(path)
                return
            for neighbor in graph[start]:
                new_path = path.copy()
                new_path.append(neighbor)
                dfs(graph, start=neighbor, end=end, path=new_path)

        dfs(graph, 0, len(graph) - 1, [0])
        return paths


print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
