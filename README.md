GreenRiver College Python Graphics Library, 2017

See Docs directory for python APIs

Install:
  Download project from GitHub
  Place"Library" folder into your Python project folder. 
  
Sample code that draws a box.

      from Library import GRCGraphics as GRC

      def main():

          # define size of graphics window
          windowWidth = 300
          windowHeight = 300


          # Define the graphics window object
          gWindow = GRC.GraphicsWindow("Title of window: Box", windowWidth, windowHeight)

          # set boarder Color of box object
          Color = "Black"

          #define a polygon object as a box
          polygon = GRC.Polygon(GRC.Point(10, 10), GRC.Point(125, 10), GRC.Point(125,125), GRC.Point(10,125))

          #Grahpic window to box object
          polygon.draw(gWindow)

          #click on window to close\exit
          gWindow.waitForClick()


      # call main function
      main()
