from typing import List
from networkx import draw_networkx, Graph, DiGraph, draw_networkx_nodes, spring_layout, draw_networkx_edges
from matplotlib.pyplot import show


def visualize_directed(edges: List, weighted: bool = False):
    visualize(DiGraph(), edges, weighted)


def visualize_undirected(edges: List, weighted: bool = False):
    visualize(Graph(), edges, weighted)


def visualize(G: Graph | DiGraph, edges: List, weighted: bool):
    if weighted:
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
        G.add_weighted_edges_from(edges)
        draw_networkx_nodes(G, spring_layout(G, seed=7))
        draw_networkx_edges(G, spring_layout(G, seed=7), width=6, alpha=0.5, edge_color="b", style="dashed")
    else: 
        G.add_edges_from(edges)
        draw_networkx(G)
    show()


