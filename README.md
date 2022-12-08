# P!ctureTh@t_Final
The pedagogical password security visualizer!
The inputted text or password is matched using a modified version of the Knuth-Morris-Pratt string matching algorithm to find a best fit password from the 
specified password list.
(Default list is RockYou.txt, but custom lists can be uploaded into ./passwordLists)

The search algorithm calculates a similarity coefficient for the matching password. By all means, if the similarity coefficient is high, DO NOT USE YOUR PASSWORD IN REAL LIFE.

Once obtainted, the password is put through both a XOR cipher and Huffman encoding to produce two distinct ciphertexts. These are then converted to RGB values through 
custom coloration algorithms. Each color (representing a character) is then displayed as a color bar in the varation gradient.

To terminate the program and save the password pictures, simply press space while the pyGame window is focused. Pictures will be in the ./images directory.
