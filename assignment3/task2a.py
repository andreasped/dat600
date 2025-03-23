import heapq

def prim_mst(graph, start_node):
    mst = []
    visited = set()
    min_heap = [(0, start_node, None)]
    total_cost = 0

    while min_heap and len(visited) < len(graph):
        weight, node, prev = heapq.heappop(min_heap)
        
        if node in visited:
            continue

        visited.add(node)
        if prev is not None:
            mst.append((prev, node, weight))
            total_cost += weight

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (cost, neighbor, node))

    if len(visited) == len(graph):
        return mst, total_cost
    else:
        return None, float("inf")  # Return infinite cost if the graph is disconnected

graph = {
    'A': [('D', 1), ('B', 5)],
    'B': [('A', 5), ('D', 4), ('H', 8)],
    'C': [('D', 2), ('G', 6)],
    'D': [('A', 1), ('B', 4), ('C', 2), ('E', 2), ('F', 4)],
    'E': [('D', 2), ('H', 8)],
    'F': [('D', 4), ('G', 9), ('H', 7)],
    'G': [('C', 6), ('F', 9)],
    'H': [('B', 8), ('E', 8), ('F', 7)]
}

start_node = 'A'
mst, cost = prim_mst(graph, start_node)
if mst:
    print("Minimum Spanning Tree (MST) edges:", mst)
    print("Total cost of MST:", cost)