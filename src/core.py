import pygame, sys, math
from pygame.locals import *
from xortest import modifiedXOR
from kmptest import kmp
from huffmantest import *

SIZE = (500, 500)
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
KEY = "HDS"
# WIDTH = 10


class Board:
    # initializes the board
    def __init__(self, size=SIZE):
        self.size = size

    def window(self):
        # creates the window
        pygame.init()
        pygame.display.set_caption("Password Colorizer")

        self.background = pygame.Surface(self.size)
        self.background.fill((0, 0, 0))
        self.screen = pygame.display.set_mode(self.size)


class ColorBar:  # the width will depend on the length of the XORed string, basically (SIZE[1]/len(XORed string))
    # initialize the color bars
    def __init__(self, height=SIZE[1] / 2, color=WHITE):
        self.height = height
        self.color = color


class Universe:
    # initialize the universe
    def __init__(self):
        self.board = Board()
        self.bars = []  # vector of color bars
        self.running = True

    def hexToRGB(self, hexString):
        # convert a hex string to RGB
        # this is the backend for the color bars
        hexString = hexString[2:]
        r = int(hexString[0:2], 16)
        g = int(hexString[2:4], 16)
        b = int(hexString[4:6], 16)
        return (r, g, b)

    def colorFromLetter(self, letter):
        # convert a letter to a color
        # this is the backend for the color bars
        # convert the letter to binary
        value = ord(letter)
        value -= 33
        value /= 94
        value *= 255
        value = math.trunc(value)
        h = int(str(value) * 3)
        h = hex(h)
        # h = h[2:8]
        return self.hexToRGB(h)

    def colorFromNumber(self, num):
        # convert a number to a color
        # this is the backend for the color bars
        # convert the number to binary
        value = num + 10
        h = int(str(value) * 9)
        h = hex(h)
        # h = h[2:8]
        return self.hexToRGB(h)

    def returnHuffmanString(self, pt):
        # return the huffman string
        # this is the backend for the huffman string
        freq = Counter(pt)
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        node = makeHuffmanTree(freq)
        encodedString = Huffman(node)
        return encodedString

    def hexifyHuffman(self, huffmanString):
        # convert the huffman string to hex
        # this is the backend for the huffman string
        hexString = ""
        for i in huffmanString:
            hexString += hex(ord(i))[2:]
        return hexString

    def update(self, pt, ct):
        # update the universe
        # wont really need this, but we could probably show the bars while the password is being xored, that'd be pretty cool
        # don't do any visual stuff here, its all backend
        ###rules###
        # this is the backend for the bars being updated as the encryption algos run
        # empty the bars vector
        self.bars = []
        barGroup = []
        for char in pt:
            color = self.colorFromLetter(char)
            barGroup.append(ColorBar(color=color))
        self.bars.append(barGroup)
        barGroup = []
        for char in ct:
            color = self.colorFromLetter(char)
            barGroup.append(ColorBar(color=color))
        self.bars.append(barGroup)

        barGroup = []
        encodedString = self.returnHuffmanString(pt)
        for i in encodedString:
            bbit = encodedString[i]
            dec = int(bbit, 2)
            color = self.colorFromNumber(dec)
            barGroup.append(ColorBar(color=color))
        self.bars.append(barGroup)

    def draw(self, screen, background):
        # draw the universe
        # fill the screen with white
        screen.blit(background, (0, 0))
        # draw the bars
        # draw pt
        width = (SIZE[0] / 2) / len(self.bars[0])
        xPos = 0
        for bar in self.bars[0]:
            pygame.draw.rect(screen, bar.color, (xPos * width, 0, width, bar.height))
            xPos += 1
        # draw ct
        xPos = 0
        for bar in self.bars[1]:
            pygame.draw.rect(
                screen, bar.color, (xPos * width + 250, 0, width, bar.height)
            )
            xPos += 1

        xPos = 0
        for bar in self.bars[2]:
            pygame.draw.rect(screen, bar.color, (xPos * width, 250, width, bar.height))
            xPos += 1
        # do all the visual stuff here on the pygame board

    def run(self, plaintext, ct, chars):
        # run the universe
        pt = plaintext
        picNames = ["XOR_pt", "XOR_ct", "Huffman"]

        self.board.window()
        screen = self.board.screen
        background = self.board.background
        clock = pygame.time.Clock()

        def savePics():
            rect = pygame.Rect(0, 0, 250, 250)
            sub = screen.subsurface(rect)
            pygame.image.save(sub, "images/" + chars + "_" + picNames[0] + ".png")
            rect = pygame.Rect(250, 0, 250, 250)
            sub = screen.subsurface(rect)
            pygame.image.save(sub, "images/" + chars + "_" + picNames[1] + ".png")
            rect = pygame.Rect(0, 250, 250, 250)
            sub = screen.subsurface(rect)
            pygame.image.save(sub, "images/" + chars + "_" + picNames[2] + ".png")

        while self.running:
            # this is the event loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    savePics()
                    pygame.quit()
                    sys.exit()
                # if key q down, quit
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        savePics()
                        pygame.quit()
                        sys.exit()
            self.update(pt, ct)
            self.draw(screen, background)
            pygame.display.update()
            clock.tick(60)


def takeInput():  # this can be in CLI or have a way to display this on the window, should prob be part of Universe class
    print("Enter characters to be in password: ")
    characters = input()
    return characters
    # use search algorithm to find best fit password in rockyou.txt


def calculateSimilarityCoefficient(password, numHits):
    n = len(password)
    return numHits * 10 / n


# driver
def main():

    list = "rockyou100k"
    path = "passwordLists/" + list + ".txt"

    # chars = "dan"
    chars = takeInput()

    passwords = []
    # open '../passwordLists/top100.txt
    with open(path, "r", encoding="utf8") as f:
        for line in f:
            passwords.append(line.strip())

    maxSimilarity = 0
    bestPassword = ""
    for ind, password in enumerate(passwords):
        x = kmp(chars, password)
        if x:
            # print("Match found: " + password)
            simCoef = calculateSimilarityCoefficient(password, len(x))
            # print("Similarity Coefficient: " + str(simCoef))
            if simCoef > maxSimilarity:
                maxSimilarity = simCoef
                bestPassword = password  # earliest index of match is used as tiebreak
    print("Best password: " + bestPassword)
    print("Similarity Coefficient: " + str(maxSimilarity))

    # xor the password with the key
    # print(huffman(bestPassword))

    pt = bestPassword
    ct_xor = modifiedXOR(pt, KEY)
    # ct_huffman = huffman(pt)
    # put bestPassword through modifiedXOR and huffman tree

    universe = Universe()
    universe.run(pt, ct_xor, chars)
    # will run takeinput(), search algorithm and store the appropriate password, run XOR with input string,
    # create color bars based on the XORed string, and display the password


if __name__ == "__main__":
    main()
