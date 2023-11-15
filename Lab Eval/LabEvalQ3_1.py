import networkx as nx
import matplotlib.pyplot as plt
import time
import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def edge_marking_mst(self):
        result = []

        self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while len(result) < self.V - 1:
            u, v, w = self.graph.pop()

            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

    def visualize_graph(self):
        G = nx.Graph()
        for u, v, w in self.graph:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Original Graph")
        plt.show()

        mst_edges = self.edge_marking_mst()
        mst_graph = nx.Graph()
        for u, v, w in mst_edges:
            mst_graph.add_edge(u, v, weight=w)

        pos = nx.spring_layout(mst_graph)
        labels = nx.get_edge_attributes(mst_graph, 'weight')
        nx.draw(mst_graph, pos, with_labels=True, node_size=700, node_color='lightgreen')
        nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)
        plt.title("Minimum Spanning Tree (MST)")
        plt.show()

def measure_time_complexity():
    graph_sizes = list(range(5, 101, 5))
    execution_times = []

    for size in graph_sizes:
        g = Graph(size)
        for _ in range(size * 2):
            u, v, w = random.randint(0, size - 1), random.randint(0, size - 1), random.randint(1, 100)
            g.add_edge(u, v, w)

        start_time = time.time()
        mst = g.edge_marking_mst()  # Fix: Store the MST
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)

    plt.plot(graph_sizes, execution_times, marker='o')
    plt.title("Time Complexity of Edge-Marking Algorithm")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution Time (s)")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    measure_time_complexity()
