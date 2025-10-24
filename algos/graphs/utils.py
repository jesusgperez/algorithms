from typing import List
from networkx import draw_networkx, Graph, DiGraph
from matplotlib.pyplot import show


def visualize_directed(edges: List):
    visualize(DiGraph(), edges)


def visualize_undirected(edges: List):
    visualize(Graph(), edges)


def visualize(G: Graph | DiGraph, edges: List):
    G.add_edges_from(edges)
    draw_networkx(G)
    show()


