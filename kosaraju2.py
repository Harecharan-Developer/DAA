import networkx as nx
import matplotlib.pyplot as plt

def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

def get_adjacent_nodes(graph, u):
    return graph.get(u, [])

def get_all_nodes(graph):
    return graph.keys()

def dfs(graph, u, visited, stack):
    visited.add(u)
    for v in get_adjacent_nodes(graph, u):
        if v not in visited:
            dfs(graph, v, visited, stack)
    stack.append(u)

def dfs_transpose(graph, u, visited, scc):
    visited.add(u)
    scc.append(u)
    for v in get_adjacent_nodes(graph, u):
        if v not in visited:
            dfs_transpose(graph, v, visited, scc)

def find_scc(graph):
    visited = set()
    stack = []

    for node in get_all_nodes(graph):
        if node not in visited:
            dfs(graph, node, visited, stack)

    transposed_graph = transpose_graph(graph)
    visited = set()
    scc_list = []

    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs_transpose(transposed_graph, node, visited, scc)
            scc_list.append(scc)

    return scc_list

def transpose_graph(graph):
    transposed = {}
    for u in get_all_nodes(graph):
        for v in get_adjacent_nodes(graph, u):
            add_edge(transposed, v, u)
    return transposed

# Create a graph
graph = {}
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 1, 4)
add_edge(graph, 4, 5)
add_edge(graph, 5, 6)
add_edge(graph, 6, 4)
add_edge(graph, 4, 7)
add_edge(graph, 7, 8)
add_edge(graph, 8, 9)
add_edge(graph, 9, 10)
add_edge(graph, 10, 7)

# Find strongly connected components
sccs = find_scc(graph)

# Print strongly connected components
print("Strongly Connected Components:")
for i, scc in enumerate(sccs):
    print(f"Component {i + 1}: {scc}")

# Create a NetworkX graph for visualization
G = nx.DiGraph()
for scc in sccs:
    for u in scc:
        for v in get_adjacent_nodes(graph, u):
            if v in scc:
                G.add_edge(u, v)

# Visualize the graph
pos = nx.spring_layout(G)
colors = ['red', 'green', 'blue', 'yellow', 'orange']  # Define colors for each component

nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
for i, scc in enumerate(sccs):
    nx.draw_networkx_nodes(G, pos, nodelist=scc, node_color=colors[i % len(colors)])
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray')
nx.draw_networkx_labels(G, pos)
plt.show()
