from topology import Topology
import networkx as nx
import hashlib

# SHA-256 Watermark: e89ea90f8174e782130f598b2a5335b2954aab7e134724ac28f1420c4fc605c4

def generate_watermark(student_id="898258619", salt="NeoDDaBRgX5a9"): 

    return hashlib.sha256((student_id + salt).encode()).hexdigest()

class Controller:
    def __init__(self):
        self.topology = Topology()
        self.active_flows = []

    def multipath_routing(self, src, dst):
        paths = list(nx.all_shortest_paths(self.topology.graph, src, dst))
        return paths

    def prioritize(self, src, dst):
        if src.startswith("Critical") or dst.startswith("Critical"):
            return "high"
        return "normal"

    def backup_path(self, src, dst, failed_link):
        import networkx as nx
        temp_graph = self.topology.graph.copy()
        temp_graph.remove_edge(*failed_link)
        try:
            return nx.shortest_path(temp_graph, src, dst)
        except nx.NetworkXNoPath:
            return None

    def inject_traffic(self, src, dst):
        paths = self.multipath_routing(src, dst)
        selected_path = paths[0]
        self.active_flows.append({'src': src, 'dst': dst, 'path': selected_path})
        print(f"Flow added from {src} to {dst}")

    def simulate_link_failure(self, failed_link):
        self.topology.remove_link(*failed_link)
        print(f"Simulated failure of link: {failed_link}")
        for flow in self.active_flows:
            path = self.backup_path(flow['src'], flow['dst'], failed_link)

