from Library import GRCGraphics as GRC
from Library import nrnoble as Util
import json
import pickle

#https://docs.python.org/2/tutorial/inputoutput.html

import random

windowWidth = 502
windowHeight = 268
interval = .1
Color = random.choice(Util.Colors)
gWindow1 = GRC.GraphicsWindow("Image Window-1", windowWidth, windowHeight)
background2 = GRC.Image(GRC.Point(251, 134), ".\\Content\\whitebackground.png")

def main():

    background2.draw(gWindow1)

    file = open('.\\Content\\icecave.pkle', 'rb+')
    pixels2 = pickle.load(file)
    file.close()

    random.shuffle(pixels2)

    while len(pixels2) > 0:
        pix = pixels2.pop()
        background2.setPixel(pix.x, pix.y, pix.rgb)
        gWindow1.update()



def color_rgb(r, g, b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r, g, b)


main()

Util.pause(gWindow1)