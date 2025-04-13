import pulp
from collections import defaultdict

nodes = {'s', 'v1', 'v2', 'v3', 'v4', 'v5', 't'}
source = 's'
sink = 't'

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
    ('v5', 't', 10),
]

prob = pulp.LpProblem("MaximumFlow", pulp.LpMaximize)

# Create flow variables for each edge. (Lowbound is for non negative constraint)
flow = {(u, v): pulp.LpVariable(f"f_{u}_{v}", lowBound=0) for (u, v, c) in edges}

# Objective:
prob += pulp.lpSum(flow[(u, v)] for (u, v, c) in edges if u == source)

#Constraints:

#Capacity
for (u, v, c) in edges:
    prob += flow[(u, v)] <= c

#Flow
flowIn = defaultdict(list)
flowOut = defaultdict(list)
for (u, v, _) in edges:
    flowOut[u].append((u, v))
    flowIn[v].append((u, v))

for node in nodes - {source, sink}:
    prob += (
        pulp.lpSum(flow[e] for e in flowIn[node]) ==
        pulp.lpSum(flow[e] for e in flowOut[node])
    )

prob.solve()

print(f"Maximum flow value: {pulp.value(prob.objective)}")

for (u, v), var in flow.items():
    if var.varValue > 0:
        print(f"Flow for edge ({u}, {v}): {var.varValue}")
