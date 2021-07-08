from graph.graph import Graph, Edge, Vertex

def depth_first_search(visited, graph, node): 
        visited = []
        graph = Graph
        neighbors = graph.get_neighbors()
        traversal = True

        while traversal:
            for neighbors in graph[node]:
                visited.add(node)
                depth_first_search(visited, graph, neighbors)
                print(visited, node)
