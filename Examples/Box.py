from Library import GRCGraphics as GRC
from Library import nrnoble as Util


import random

Colors =['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Orange', 'Pink', 'Purple', 'Gold', 'Silver', 'Gray', 'Maroon']

def main():
    windowWidth = 300
    windowHeight = 300

    Color = random.choice(Colors)
    gWindow = GRC.GraphicsWindow("Box", windowWidth, windowHeight)
    interval = .25
    polygon1 = GRC.Polygon(GRC.Point(10, 10), GRC.Point(125, 10), GRC.Point(125,125), GRC.Point(10,125))
    polygon1.draw(gWindow)
    Util.pause(gWindow)




main()
