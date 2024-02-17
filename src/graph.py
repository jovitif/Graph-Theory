class Graph:
    def __init__(self):
        self.node = set()
        self.edge = set()

    def create_node(self, node):
        self.node.add(node)

    def create_edge(self, origin, destiny):
        self.edge.add((origin, destiny))
