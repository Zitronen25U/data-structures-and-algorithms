class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return tuple(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        if len(self.adjacency_list) == 0:
            return None
        return len(self.adjacency_list)

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Vertex:
    def __init__(self, value):
        self.value = value
