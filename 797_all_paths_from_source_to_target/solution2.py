graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [],
}


def allPathsSourceTarget(graph):
    paths = []

    def dfs(graph, start, end, path):
        if start == end:
            paths.append(path)
            return
        neighbors = graph[start]
        for neighbor in neighbors:
            dfs(graph, neighbor, end, f"{path},{neighbor}")

    dfs(graph, 0, len(graph) - 1, "0")
    return [[int(i) for i in path.split(",")] for path in paths]


print(allPathsSourceTarget(graph))
