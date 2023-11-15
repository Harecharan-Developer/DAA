import networkx as nx
import heapq
import time
import matplotlib.pyplot as plt

# Step 1: Input Reading (for synthetic graph, skip this step)
N = 1000  # Number of cities
M = 2000  # Number of possible routes between cities
edges = []

# For synthetic graphs using NetworkX
def generate_synthetic_graph(N):
    G = nx.Graph()
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            weight = i * j % 10 + 1
            G.add_edge(i, j, weight=weight)
    return G

# Step 2: Create the Graph (Adjacency Matrix Representation)
def create_adjacency_matrix(graph):
    INF = float('inf')
    adj_matrix = [[INF] * (N + 1) for _ in range(N + 1)]
    for u, v, t in graph.edges(data=True):
        adj_matrix[u][v] = t['weight']
        adj_matrix[v][u] = t['weight']
    return adj_matrix

# Step 2: Create the Graph (Priority Queue Representation)
def create_priority_queue(graph):
    pq = [(0, 1)]  # (distance, city)
    distances = [float('inf')] * (N + 1)
    distances[1] = 0
    return pq, distances

# Step 3: Implement Dijkstra's Algorithm (Adjacency Matrix Representation)
def dijkstra_adjacency_matrix(adj_matrix):
    INF = float('inf')
    distances = [INF] * (N + 1)
    visited = [False] * (N + 1)
    distances[1] = 0

    for _ in range(N):
        u = -1
        for i in range(1, N + 1):
            if not visited[i] and (u == -1 or distances[i] < distances[u]):
                u = i

        visited[u] = True
        for v in range(1, N + 1):
            if not visited[v] and adj_matrix[u][v] != INF:
                distances[v] = min(distances[v], distances[u] + adj_matrix[u][v])

    return distances

# Step 3: Implement Dijkstra's Algorithm (Priority Queue Representation)
def dijkstra_priority_queue(pq, distances, adj_matrix):
    while pq:
        dist, u = heapq.heappop(pq)
        if dist > distances[u]:
            continue
        for v in range(1, N + 1):
            if adj_matrix[u][v] != float('inf') and distances[u] + adj_matrix[u][v] < distances[v]:
                distances[v] = distances[u] + adj_matrix[u][v]
                heapq.heappush(pq, (distances[v], v))

# Step 4: Generate Output
def generate_output(distances):
    print(N, N - 1)
    for y in range(2, N + 1):
        print(1, y, distances[y])

# Step 5: Measure Execution Time and Plot
def measure_and_plot_timing(graph_sizes):
    adjacency_matrix_times = []
    priority_queue_times = []

    for size in graph_sizes:
        # Generate a synthetic graph with 'size' nodes
        G = generate_synthetic_graph(size)

        # For Adjacency Matrix Representation
        adj_matrix = create_adjacency_matrix(G)
        start_time = time.time()
        dijkstra_adjacency_matrix(adj_matrix)
        adjacency_matrix_times.append(time.time() - start_time)

        # For Priority Queue Representation
        pq, distances = create_priority_queue(G)
        start_time = time.time()
        dijkstra_priority_queue(pq, distances, adj_matrix)
        priority_queue_times.append(time.time() - start_time)

    # Plot the timing vs. number of nodes
    plt.plot(graph_sizes, adjacency_matrix_times, label='Adjacency Matrix')
    plt.plot(graph_sizes, priority_queue_times, label='Priority Queue')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Execution Time vs. Number of Nodes')
    plt.show()

# Specify the graph sizes you want to test
graph_sizes_to_test = [100, 200, 300, 400, 500]

# Measure and plot the timing
measure_and_plot_timing(graph_sizes_to_test)
