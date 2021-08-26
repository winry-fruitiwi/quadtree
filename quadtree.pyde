# Winry/Tigrex, 8/25/2021
# Inspired by Daniel Shiffman. The quadtree makes collision checks more efficient.
# 
# versions:
# v0.01:  rectangle, point, testing, maybe mousedrag
# v0.0:   quadtree insert
# v0.0:   quadtree subdivide
# v0.0:   quadtree basic test, contains
# v0.0:   quadtree query
# v0.0:   collision detection


# this describes an object that is literally just a point, but a more powerful point
# because it is active in a quadtree. Necessary for testing, but otherwise not so important.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        pushMatrix()
        translate(self.x, self.y)
        stroke(0, 0, 100, 80)
        strokeWeight(3)
        point(0, 0)
        popMatrix()


# this describes an object that is the boundary of a quadtree. Very important!
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w # width
        self.h = h # height
    
    def show(self):
        pushMatrix()
        translate(self.x, self.y)
        stroke(0, 0, 100, 80)
        noFill()
        rect(0, 0, self.w, self.h)
        popMatrix()


def setup():
    global points, rectangles
    colorMode(HSB, 360, 100, 100, 100)
    
    points = []
    rectangles = []
    size(700, 700)
    #points.append(Point(width/2, height/2))
    rectangles.append(Rectangle(0, 0, width, height))


def draw():
    global points, rectangles
    background(220, 79, 32)
    for p in points:
        p.show()
    
    
    for r in rectangles:
        r.show()


# for this function, we just want to drag the mouse around and it'll leave behind
# a streak of white points
def mouseDragged():
    global points, rectangles
    points.append(Point(mouseX, mouseY))
