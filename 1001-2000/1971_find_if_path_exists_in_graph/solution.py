from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n <= 1:
            return True
        graph = self.make_graph(edges)
        stack = [source]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                print(curr)
            for neighbor in graph[curr]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    stack.append(neighbor)

        return False

    def make_graph(self, edges: list[list[int]]):
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        return graph
