from collections import defaultdict
from typing import List

edges = [[1, 2], [2, 3], [4, 2]]


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int | None:
        """
        1. the center is the only that has >1 edge
        2. the center is connected to all other nodes
        3. any 2 edges must have the common node which is the center
        """

        graph = self.make_graph(edges)
        nodes = list(graph.keys())

        for i in range(len(nodes)):
            node = nodes[i]
            other_nodes = nodes[:i] + nodes[i + 1 :]

            if set(graph[node]) == set(other_nodes) and len(graph[node]) > 1:
                return node
        return None

    def make_graph(self, edges: list[list[int]]):
        graph = defaultdict(set)
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)

        return graph
