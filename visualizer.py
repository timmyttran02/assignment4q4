import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, flows=None):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)

    if flows:
        for flow in flows:
            path = flow['path']
            edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='r', width=2)
    plt.show()
