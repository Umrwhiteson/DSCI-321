class VersatileDigraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.edge_names = {}

    def add_node(self, node_id, node_value=0):
        if node_id not in self.nodes:
            self.nodes[node_id] = node_value
            self.edges[node_id] = {}
            self.edge_names[node_id] = {}

    def add_edge(
        self,
        start_node_id,
        end_node_id,
        start_node_value=None,
        end_node_value=None,
        edge_name=None,
        edge_weight=1
    ):
        if edge_name is None:
            edge_name = end_node_id

        names = self.edge_names.get(start_node_id, {})

        if edge_name in names and names[edge_name] != end_node_id:
            raise ValueError(
                "Edges from the same start node must have unique names."
            )

        if start_node_id not in self.nodes:
            self.add_node(start_node_id)

        if end_node_id not in self.nodes:
            self.add_node(end_node_id)

        if start_node_value is not None:
            self.nodes[start_node_id] = start_node_value

        if end_node_value is not None:
            self.nodes[end_node_id] = end_node_value

        if end_node_id in self.edges[start_node_id]:
            old_name = self.edges[start_node_id][end_node_id]["name"]
            del self.edge_names[start_node_id][old_name]

        self.edges[start_node_id][end_node_id] = {
            "name": edge_name,
            "weight": edge_weight
        }

        self.edge_names[start_node_id][edge_name] = end_node_id

    def get_nodes(self):
        return list(self.nodes)

    def get_edge_weight(self, start_node_id, end_node_id):
        return self.edges[start_node_id][end_node_id]["weight"]

    def get_node_value(self, node_id):
        return self.nodes[node_id]

    def get_edge_name(self, start_node_id, end_node_id):
        return self.edges[start_node_id][end_node_id]["name"]

    def get_end_node(self, start_node_id, edge_name):
        return self.edge_names[start_node_id][edge_name]

    def print_graph(self):
        for node_id, node_value in self.nodes.items():
            print(f"Node {node_id} with value {node_value}")

        for start_node_id, outgoing_edges in self.edges.items():
            for end_node_id, edge in outgoing_edges.items():
                print(
                    f"Edge from {start_node_id} to {end_node_id} "
                    f"with weight {edge['weight']} "
                    f"and name {edge['name']}"
                )
if __name__ == "__main__":
    graph = VersatileDigraph()

    graph.add_node("A", 10)

    graph.add_edge(
        "A", "B",
        edge_weight=5,
        edge_name="edge1"
    )

    graph.print_graph() 
    print(graph.get_nodes())
    print(graph.get_node_value("A"))
    print(graph.get_edge_weight("A", "B"))
    print(graph.get_edge_name("A", "B"))
    print(graph.get_end_node("A", "edge1"))               
