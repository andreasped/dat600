def remove_cycles(graph):
    def dfs(node, visited, rec_stack, back_edges):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:  # Forward Edge
                if dfs(neighbor, visited, rec_stack, back_edges):
                    return True
            elif rec_stack[neighbor]:  # Back Edge (Cycle detected)
                back_edges.append((node, neighbor))

        rec_stack[node] = False
        return False

    def detect_and_remove_cycles(graph):
        visited = {node: False for node in graph}
        rec_stack = {node: False for node in graph}
        back_edges = []

        for node in graph:
            if not visited[node]:
                dfs(node, visited, rec_stack, back_edges)

        for u, v in back_edges:
            graph[u].remove(v)  # Remove one edge per cycle to break it

        return len(back_edges) > 0  # If true, the edges were removed

    while detect_and_remove_cycles(graph):
        pass

    return graph

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['A', 'E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': ['C'],
    'J': ['I']
}

print(remove_cycles(graph))