from Library.BaseGraphicObject import *

from Library.BaseGlobals import *


class Text(GraphicsObject):
    def __init__(self, p, text):
        GraphicsObject.__init__(self, ["justify", "fill", "text", "font"])
        self.setText(text)
        self.anchor = p.clone()
        self.setFillColor(DEFAULT_CONFIG['outline'])
        self.setOutline = self.setFillColor

    def __repr__(self):
        return "Text({}, '{}')".format(self.anchor, self.getText())

    def _draw(self, canvas, options):
        p = self.anchor
        x, y = canvas.toScreen(p.x, p.y)
        return canvas.create_text(x, y, options)

    def _move(self, dx, dy):
        self.anchor.move(dx, dy)

    def clone(self):
        other = Text(self.anchor, self.config['text'])
        other.config = self.config.copy()
        return other

    def setText(self, text):
        self._reconfig("text", text)

    def getText(self):
        return self.config["text"]

    def getAnchor(self):
        return self.anchor.clone()

    def setFont(self, face):
        if face in ['helvetica', 'arial', 'courier', 'times roman', 'NealNoble_3']:
            f, s, b = self.config['font']
            self._reconfig("font", (face, s, b))
        else:
            raise GraphicsError(BAD_OPTION)

    def setFontSize(self, size):
        if 5 <= size <= 36:
            f, s, b = self.config['font']
            self._reconfig("font", (f, size, b))
        else:
            raise GraphicsError(BAD_OPTION)

    def setFontStyle(self, style):
        if style in ['bold', 'normal', 'italic', 'bold italic']:
            f, s, b = self.config['font']
            self._reconfig("font", (f, s, style))
        else:
            raise GraphicsError(BAD_OPTION)

    def setTextColor(self, color):
        self.setFillColor(color)

def demo():

    import random, os, sys, inspect, pickle
    from Library import GRCGraphics as GRC

    windowWidth = 300
    windowHeight = 25
    interval = 1
    Color = random.choice(GRC.COLORS)
    gWindow = GRC.GraphicsWindow("Text Demo", windowWidth, windowHeight)

    scrollText = GRC.Text(GRC.Point(500, 15), "Scroll Demo.... ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    scrollText.setTextColor("Blue")
    scrollText.setFontSize(12)
    gWindow.addItem(scrollText)
    gWindow.update()

    for moveX in range(1,700,1):
        scrollText.move(-1,0)
        gWindow.redraw()
        GRC.time.sleep(.01)

    Util.pause(gWindow)

