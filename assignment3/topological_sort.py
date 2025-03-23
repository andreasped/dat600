from collections import deque

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    zero_in_degree = deque([node for node in graph if in_degree[node] == 0])

    sorted_order = []
    while zero_in_degree:
        current = zero_in_degree.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    # Check for cycles, we want DAG
    if len(sorted_order) != len(graph):
        raise ValueError("Graph has at least one cycle and is not a DAG")

    return sorted_order

if __name__ == '__main__':
    dag = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['E', 'F'],
        'D': ['E', 'F'],
        'E': ['F', 'G', 'J'],
        'F': ['G', 'H', 'J'],
        'G': [],
        'H': ['I'],
        'I': [],
        'J': ['I']
    }

    print(topological_sort(dag))