class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __le__(self, other):
        return self.freq <= other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __ge__(self, other):
        return self.freq >= other.freq

class Huffman:
    def __init__(self, nodes):
        self.root = self.build_huffman_tree(nodes)
        self.encoding = {}
        self.build_encoding(self.root, "")

    def build_huffman_tree(self, nodes):
        while len(nodes) > 1:
            nodes.sort()
            x1 = nodes.pop(0)
            x2 = nodes.pop(0)
            total_freq = x1.freq + x2.freq
            n = Node(None, total_freq)
            n.left = x1
            n.right = x2
            nodes.append(n)
        return nodes[0] if nodes else None

    def build_encoding(self, node, code):
        if node:
            if node.val is not None:
                self.encoding[node.val] = code
            self.build_encoding(node.left, code + "0")
            self.build_encoding(node.right, code + "1")

    def encode(self, text):
        encoded_text = ""
        for char in text:
            if char in self.encoding:
                encoded_text += self.encoding[char]
            else:
                print("Character  not in Huffman encoding")
        return encoded_text

    def decode(self, encoded_text):
        decoded_text = ""
        current_node = self.root
        for i in encoded_text:
            if i == '0':
                current_node = current_node.left
            elif i == '1':
                current_node = current_node.right

            if current_node.val is not None:
                decoded_text += current_node.val
                current_node = self.root

        return decoded_text

arr = [("a", 5), ("b", 10), ("c", 15), ("d", 25), ("e", 30), ("f", 50)]
nodes = [Node(val, freq) for val, freq in arr]
huffman_tree = Huffman(nodes)

text_to_encode = "abcde"
encoded_text = huffman_tree.encode(text_to_encode)
decoded_text = huffman_tree.decode(encoded_text)

print("Original text:", text_to_encode)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
