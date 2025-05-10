import networkx as nx

class Topology:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def remove_node(self, node):
        self.graph.remove_node(node)

    def add_link(self, node1, node2, capacity=1):
        self.graph.add_edge(node1, node2, weight=1, capacity=capacity)

    def remove_link(self, node1, node2):
        self.graph.remove_edge(node1, node2)

    def shortest_path(self, src, dst):
        return nx.shortest_path(self.graph, source=src, target=dst, weight="weight")
