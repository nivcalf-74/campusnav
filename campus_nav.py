import networkx as nx
import math

class CampusNavigator:
    def __init__(self, nodes_file, edges_file):
        self.G = nx.DiGraph()
        self.load_nodes(nodes_file)
        self.load_edges(edges_file)
        self.nodes_data = {}
        
    def load_nodes(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[1:], 1):
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    node_id = parts[0].strip()
                    name = parts[1].strip()
                    floor = parts[2].strip()
                    keywords = parts[3].strip() if len(parts) > 3 else ""
                    self.G.add_node(node_id, name=name, floor=floor, keywords=keywords)
                    self.nodes_data[node_id] = {'name': name, 'floor': floor, 'keywords': keywords}
    
    def load_edges(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    src = parts[0].strip()
                    tgt = parts[1].strip()
                    time = int(parts[2].strip())
                    dist = int(parts[3].strip()) if len(parts) > 3 else 0
                    instruction = parts[4].strip() if len(parts) > 4 else ""
                    self.G.add_edge(src, tgt, time=time, distance=dist, instruction=instruction)
    
    def find_shortest_path(self, source, target, weight='time'):
        try:
            path = nx.shortest_path(self.G, source, target, weight=weight)
            distance = nx.shortest_path_length(self.G, source, target, weight=weight)
            return path, distance
        except nx.NetworkXNoPath:
            return None, None
        except nx.NodeNotFound:
            return None, None
    
    def get_path_details(self, path):
        if not path or len(path) < 2:
            return []
        
        details = []
        for i in range(len(path) - 1):
            src = path[i]
            tgt = path[i + 1]
            edge_data = self.G[src][tgt]
            
            details.append({
                'from': self.nodes_data[src]['name'],
                'to': self.nodes_data[tgt]['name'],
                'time': edge_data.get('time', 0),
                'distance': edge_data.get('distance', 0),
                'instruction': edge_data.get('instruction', '')
            })
        return details

# דוגמה לשימוש:
if __name__ == "__main__":
    nav = CampusNavigator('nodes.csv', 'edges.csv')
    path, total_time = nav.find_shortest_path('17', '47', weight='time')
    
    if path:
        print(f"נתיב: {' -> '.join(path)}")
        print(f"זמן כולל: {total_time} שנייות")
        details = nav.get_path_details(path)
        for i, d in enumerate(details, 1):
            print(f"שלב {i}: {d['from']} ל-{d['to']} ({d['time']}s, {d['distance']}m)")
