import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, val, label=None):
        self.val = val
        self.left = None
        self.right = None
        self.label = label

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

class Huffman:
    def __init__(self, nodes):
        self.l1 = []

        while nodes:
            self.l1.append(Node(nodes[0].val, nodes[0].label))
            nodes.pop(0)

        while len(self.l1) > 1:  
            self.l1.sort()
            x1 = self.l1.pop(0)
            x2 = self.l1.pop(0)
            total_sum = x1.val + x2.val
            n = Node(total_sum, None)
            n.left = x1
            n.right = x2
            self.l1.append(n)  

    def get_huffman_tree(self):
        return self.l1[0] if self.l1 else None

def visualize_huffman_tree(root):
    G = nx.Graph()

    def add_edges(node, parent=None):
        if node:
            G.add_node(node.val, label=node.label)
            if parent is not None:
                G.add_edge(parent.val, node.val)
            add_edges(node.left, node)
            add_edges(node.right, node)

    add_edges(root)

    pos = nx.spring_layout(G)  
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=5000, font_size=10, font_color='black')
    plt.show()

arr = [("a", 5), ("b", 10), ("c", 15), ("d", 25), ("e", 30), ("f", 50)]
nodes = [Node(val, label) for label, val in arr]
huffman_tree = Huffman(nodes).get_huffman_tree()

visualize_huffman_tree(huffman_tree)
