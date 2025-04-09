import networkx as nx

# Create the directed graph for the flow network
G = nx.DiGraph()

# Add edges to the graph with their respective capacities
G.add_edge('s', 'v1', capacity=14)
G.add_edge('v1', 'v4', capacity=21)
G.add_edge('v4', 't', capacity=20)
G.add_edge('s', 'v2', capacity=25)
G.add_edge('v2', 'v5', capacity=7)
G.add_edge('v5', 't', capacity=10)
G.add_edge('v1', 'v3', capacity=3)
G.add_edge('v3', 'v1', capacity=6)
G.add_edge('v2', 'v3', capacity=13)
G.add_edge('v4', 'v3', capacity=10)
G.add_edge('v3', 'v5', capacity=15)
G.add_edge('v5', 'v4', capacity=5)

# Compute the maximum flow using the Edmonds-Karp algorithm (default in networkx)
flow_value, flow_dict = nx.maximum_flow(G, 's', 't')

print("=" * 30)
print("Maximum Flow Analysis")
print("=" * 30)
print(f"Maximum Flow Value: {flow_value}")
print("\nFlow Distribution:")
for node, flows in flow_dict.items():
    print(f"  {node}: {flows}")

# Compute the minimum cut (bottleneck cut) using the max-flow min-cut theorem
cut_value, (set_S, set_T) = nx.minimum_cut(G, 's', 't')

print("\n" + "=" * 30)
print("Minimum Cut Analysis")
print("=" * 30)
print(f"Minimum Cut Capacity: {cut_value}")
print(f"Set S (reachable from source): {set_S}")
print(f"Set T (reachable from sink): {set_T}")

# The edges in the minimum cut
cut_edges = []
for u in set_S:
    for v in G.neighbors(u):
        if v in set_T:  # Edge from set S to set T
            cut_edges.append((u, v, G[u][v]['capacity']))

print("\nEdges in the Minimum Cut:")
for edge in cut_edges:
    print(f"  {edge[0]} -> {edge[1]} (Capacity: {edge[2]})")
print("=" * 30)
