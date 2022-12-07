# create a huffman tree to encode a string
from collections import Counter


class Node(object):
    # init with left and right
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def getChildren(self):
        return (self.left, self.right)


def Huffman(node, bString=""):
    if type(node) is str:
        return {node: bString}
    l, r = node.getChildren()
    d = dict()
    d.update(Huffman(l, bString + "0"))
    d.update(Huffman(r, bString + "1"))
    return d


def makeHuffmanTree(nodes):
    while len(nodes) > 1:
        key1, c1 = nodes[-1]
        key2, c2 = nodes[-2]
        nodes = nodes[:-2]
        node = Node(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


# s1 = "aabbbcccc"
# freq = Counter(s1)
# freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# node = makeHuffmanTree(freq)
# encodedString = Huffman(node)
# for i in encodedString:
#     print(encodedString[i], type(encodedString[i]))
