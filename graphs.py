# graphs.py

from collections import defaultdict
import logging
from os import stat_result

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, id: int) -> None:
        self.id = id
        self.adjacent = set()

    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    def __repr__(self) -> str:
        return f"Node({self.id})"

    def __hash__(self) -> int:
        return self.id


class Graph:
    def __init__(self):
        self.nodes = {}

    def get_node(self, id: int) -> Node:
        return self.nodes.get(id)

    def add_edge(self, u: int, v: int):
        logger.debug("add_edge %s, %s", u, v)
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)

        self.get_node(u).adjacent.add(self.get_node(v))

    def has_path_dsf(self, source: int, dest: int) -> tuple:
        s = self.get_node(source)
        d = self.get_node(dest)
        visited = set()
        return self._has_path_dfs(s, d, visited)

    def _has_path_dfs(self, source: Node, dest: Node, visited: set) -> tuple:
        if source.id in visited:
            return False

        visited.add(source.id)

        if source == dest:
            return True

        for n in source.adjacent:
            if self._has_path_dfs(n, dest, visited):
                return True
        return False, {}

    def has_path_bfs(self, source: int, dest: int) -> bool:
        q = []
        visited = set()
        q.append(self.get_node(source))
        dest = self.get_node(dest)

        while q:
            node = q.pop(0)
    
            if node == dest:
                return True

            if node in visited:
                continue
            
            visited.add(node)

            for child in node.adjacent:
                q.append(child)

        return False



def traverse_dfs(g: Graph, n: Node, visited=None, level=0, acc=None):
    if visited is None:
        visited = set()
    if acc is None:
        acc = defaultdict(list)

    acc[level].append(n.id)
    visited.add(n)

    for child in n.adjacent:
        traverse_dfs(g, child, visited=visited, level=level+1, acc=acc)

    return acc
    


g = Graph()

# connections = [
#     (1, 2),
#     (1, 3),
#     (2, 4),
#     (2, 5),
#     (3, 6),
#     (3, 7),
#     (4, 10),
#     (4, 20)
# ]

import random

for _ in range(100):
    u = random.randint(1, 10)
    v = random.randint(11, 100)
    g.add_edge(u, v)
    print(u, v)

# for edge in connections:
#     g.add_edge(*edge)

stats = traverse_dfs(g, g.get_node(1))
print(stats)

for l, vals in stats.items():
    print(f"Avg at level {l}: {sum(vals) / len(vals)}")
