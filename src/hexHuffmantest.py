from collections import Counter
from huffmantest import Node, Huffman, makeHuffmanTree

def returnHuffmanString(pt):
        # return the huffman string
        # this is the backend for the huffman string
        freq = Counter(pt)
        node = makeHuffmanTree(freq)
        encodedString = Huffman(node)
        huffmanString = ""
        for i in encodedString:
            huffmanString += encodedString[i]
        return huffmanString
    
def hexifyHuffman(huffmanString):
    # convert the huffman string to hex
    # this is the backend for the huffman string
    hexString = ""
    for i in huffmanString:
        hexString += hex(ord(i))[2:]
    return hexString

pt = "hello world"
bstring = ''
hexString = hexifyHuffman()
print(hexString)
