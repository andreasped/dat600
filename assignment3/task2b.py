import heapq

def prim_mst_with_constraints(graph, start_node, max_edges_per_node):
    mst = []
    visited = set()
    min_heap = [(0, start_node, None)]
    total_cost = 0
    node_edge_count = {node: 0 for node in graph}

    while min_heap and len(visited) < len(graph):
        weight, node, prev = heapq.heappop(min_heap)

        if node in visited:
            continue

        # Ensure 'D' does not exceed max edges when adding to MST
        if prev is not None:
            if node == 'D' and node_edge_count['D'] >= max_edges_per_node:
                continue
            if prev == 'D' and node_edge_count['D'] >= max_edges_per_node:
                continue

            mst.append((prev, node, weight))
            total_cost += weight
            node_edge_count[prev] += 1
            node_edge_count[node] += 1

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                # Ensure that 'D' does not exceed max edges before pushing to heap
                if node == 'D' and node_edge_count['D'] >= max_edges_per_node:
                    continue
                if neighbor == 'D' and node_edge_count['D'] >= max_edges_per_node:
                    continue

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
max_edges_per_node = 3
mst, cost = prim_mst_with_constraints(graph, start_node, max_edges_per_node)
if mst:
    print("Minimum Spanning Tree (MST) edges:", mst)
    print("Total cost of MST:", cost)
else:
    print("Graph is disconnected or constraints are not met.")