import math, pygame
from pygame.locals import *

letter = "a"
aasci = ord(letter)
aasci -= 33
aasci /= 94
aasci *= 255
dec = int(str(math.trunc(aasci)) * 3)
# convert dec to hex
h = hex(dec)
print()
print(h[2:8])
color = h[2:8]
# convert hex to rgb
r = int(color[0:2], 16)
g = int(color[2:4], 16)
b = int(color[4:6], 16)
print(r, g, b)
