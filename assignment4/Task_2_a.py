from pulp import *

prob = LpProblem("MinimumCut", LpMinimize)

nodes = ['s', 'v1', 'v2', 'v3', 'v4', 'v5', 't']

edges = [
    ('s', 'v1', 14),
    ('s', 'v2', 25),
    ('v1', 'v3', 3),
    ('v1', 'v4', 21),
    ('v2', 'v3', 13),
    ('v2', 'v5', 7),
    ('v3', 'v1', 6),
    ('v3', 'v4', 10),
    ('v3', 'v5', 15),
    ('v4', 't', 20),
    ('v5', 'v4', 5),
    ('v5', 't', 10)
]

# Create binary variables for each node
node_variables = LpVariable.dicts("Node", nodes, cat='Binary')

# Create binary variables for each edge
edge_in_cut = LpVariable.dicts("EdgeInCut", [(u,v) for (u,v,c) in edges], cat='Binary')

# Objective
prob += lpSum(c * edge_in_cut[(u,v)] for (u,v,c) in edges)

# Constraints:
prob += node_variables['s'] == 0
prob += node_variables['t'] == 1

for (u,v,c) in edges:
    prob += edge_in_cut[(u,v)] >= node_variables[v] - node_variables[u]
    prob += edge_in_cut[(u,v)] <= node_variables[v]
    prob += edge_in_cut[(u,v)] <= 1 - node_variables[u]

prob.solve()


print("Minimum Cut:", value(prob.objective))
print("Cut:")
print("S (Source side):", [n for n in nodes if value(node_variables[n]) == 0])
print("T (Sink side):", [n for n in nodes if value(node_variables[n]) == 1])
