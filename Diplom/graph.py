from __future__ import annotations
import os
import matplotlib.pyplot as plt
import numpy as np
from typing import List


class Graph:
    class Node:
        def __init__(self, val: str, parent: Graph.Node | None = None):
            self.val = val
            self.parent = parent
            self.childs = []

        def __str__(self) -> str:
            ret = ""
            for child in self.childs:
                ret += f"{self.val} {child.val}\n" + str(child)
            return ret

    def __init__(self, file_path: str):
        with open(file_path) as graph:
            edges = graph.readlines()

        edges = [edge[:-1].split(" ") for edge in edges]

        self.root: Graph.Node | None = self.create_node(edges[0][0], edges)

    def create_node(
        self, val: str, edges: List[List[str]], parent: Graph.Node | None = None
    ) -> Graph.Node | None:

        ret = self.Node(val, parent)
        if edges is None or len(edges) == 0:
            return ret

        childs = [
            edge_ind for edge_ind in range(len(edges)) if edges[edge_ind][0] == val
        ]

        for child_ind in range(len(childs)):
            child = childs[child_ind]

            child_val = edges[child][1]
            next_child = -1

            if child_ind + 1 < len(childs):
                next_child = childs[child_ind + 1]

            if next_child != -1:
                child_edges = edges[child + 1 : next_child]
            else:
                child_edges = edges[child + 1 :]

            if not ((child := self.create_node(child_val, child_edges, ret)) is None):

                ret.childs += [child]

        return ret

    def __str__(self) -> str:
        return "" if self.root is None else str(self.root)

    def save(self, file_path: str):
        with open(file_path, "w") as f:
            f.write(str(self))


def build_graph(node: Graph.Node | None, file: str, offset: int = 0):
    if node is None:
        return

    with open(file % node.val) as f:
        points = f.readlines()

    count = len(points)
    x = np.arange(offset, offset + count)
    y = np.array(points, dtype=float)

    plt.plot(x, y)

    for child in node.childs:
        build_graph(child, file, offset + count)


def generate_files(node: Graph.Node | None, file, start: float = 0):

    if node is None:
        return

    count = np.random.randint(30, 80)
    x = [start]

    for i in range(count):
        x += [x[-1] + np.random.uniform(-0.005, 0.01)]

    with open(file % node.val, "w") as f:
        f.write("\n".join([str(i) for i in x]))

    for child in node.childs:
        generate_files(child, file, x[-1])


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
    graph_file_path = "graph_0.grph"

    graph = Graph(dir_path + graph_file_path)

    graph.save(dir_path + graph_file_path)
    generate_files(graph.root, dir_path + "plot_%s.plt")
    build_graph(graph.root, dir_path + "plot_%s.plt")
    plt.show()
