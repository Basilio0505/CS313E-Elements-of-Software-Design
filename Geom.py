#  File: Geom.py

#  Description: This program will create Point, Circle, and Rectangle objects out of provided data and perform
# different functions.

#  Student Name: Basilio Bazan

#  Student UT EID: bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 09/16/2018

#  Date Last Modified: 09/17/2018

import math

class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c intersects this circle (non-zero area of overlap)
    # the only argument c is a Circle object
    # returns a boolean
    def does_intersect(self, c):
        distance = self.center.dist(c.center)
        return(distance < (self.radius + c.radius))

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribes(self, r):
        across = r.ul.dist(r.lr)/2
        x = float(r.lr.x - (r.length()/2))
        y = float(r.ul.y - (r.width()/2))
        return  Circle(across, x, y)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "radius = " + str(self.radius) + " Center: (" + str(self.center.x) + ", " + str(self.center.y) + ")"


    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return (abs(self.radius - other.radius) < tol)


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return float(self.lr.x - self.ul.x)

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return float(self.ul.y - self.lr.y)

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return (float(self.ul.y - self.lr.y) + float(self.lr.x - self.ul.x)) * 2.0

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return float(self.ul.y - self.lr.y) * float(self.lr.x - self.ul.x)

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return p.x > self.ul.x and p.x < self.lr.x and p.y < self.ul.y and p.y > self.lr.y

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return r.ul.x > self.ul.x and r.ul.y < self.ul.y and r.lr.x < self.lr.x and r.lr.y > self.lr.y

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def does_intersect(self, other):
        return self.ul.x > other.lr.x or self.lr.x < other.ul.x or self.ul.y < other.lr.y or self.lr.y > other.ul.y

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rect_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y - c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y + c.radius
        return Rectangle(ul_x,ul_y, lr_x,lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: ("+ str(self.ul.x)+", "+str(self.ul.y)+") LR: ("+str(self.lr.x)+", "\
               +str(self.lr.y)+")"

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        return self.length() == other.length() and self.width() == other.width()

def main():
    # open the file geom.txt
    file = open("./geom.txt", "r")

    # create Point objects P and Q
    line = file.readline()
    line = line.strip()
    coords = line.split()
    x = float(coords[0])
    y = float(coords[1])
    P = Point(x,y)

    line = file.readline()
    line = line.strip()
    coords = line.split()
    x = float(coords[0])
    y = float(coords[1])
    Q = Point(x,y)

    # print the coordinates of the points P and Q
    print("Coordinates of P: " + str(P))
    print("Coordinates of Q: " + str(Q))

    # find the distance between the points P and Q
    distance = P.dist(Q)
    print("Distance between P and Q: "+ str(distance))

    # create two Circle objects C and D
    line = file.readline()
    line = line.strip()
    coords = line.split()
    x = float(coords[0])
    y = float(coords[1])
    radius = float(coords[2])
    C = Circle(radius, x, y)

    line = file.readline()
    line = line.strip()
    coords = line.split()
    x = float(coords[0])
    y = float(coords[1])
    radius = float(coords[2])
    D = Circle(radius, x, y)

    # print C and D
    print("Circle C: " + str(C))
    print("Circle D: " + str(D))

    # compute the circumference of C
    circumference = C.circumference()
    print("Circumference of C: "+ str(circumference))

    # compute the area of D
    area = D.area()
    print("Area of D: "+ str(area))

    # determine if P is strictly inside C
    if C.point_inside(P):
        print("P is inside C")
    else:
        print("P in not inside C")

    # determine if C is strictly inside D
    if D.circle_inside(C):
        print("C is inside D")
    else:
        print("C is not inside D")

    # determine if C and D intersect (non zero area of intersection)
    if C.does_intersect(D):
        print("C does intersect D")
    else:
        print("C does not intersect D")

    # determine if C and D are equal (have the same radius)
    if C.__eq__(D):
        print("C is equal to D")
    else:
        print("C is not equal to D")

    # create two rectangle objects G and H
    line = file.readline()
    line = line.strip()
    coords = line.split()
    x1 = float(coords[0])
    y1 = float(coords[1])
    x2 = float(coords[2])
    y2 = float(coords[3])
    G = Rectangle(x1,y1,x2,y2)

    line = file.readline()
    line = line.strip()
    coords = line.split()
    x1 = float(coords[0])
    y1 = float(coords[1])
    x2 = float(coords[2])
    y2 = float(coords[3])
    H = Rectangle(x1, y1, x2, y2)

    # print the two rectangles G and H
    print("Rectangle G: " + str(G))
    print("Rectangle H: " + str(H))

    # determine the length of G (distance along x axis)
    length = G.length()
    print("Length of G: "+ str(length))

    # determine the width of H (distance along y axis)
    width = H.width()
    print("Width of H: "+ str(width))

    # determine the perimeter of G
    perimeter = G.perimeter()
    print("Perimeter of G: "+str(perimeter))

    # determine the area of H
    area = H.area()
    print("Area of H: "+ str(H))

    # determine if point P is strictly inside rectangle G
    if G.point_inside(P):
        print("P is inside G")
    else:
        print("P is not inside G")

    # determine if rectangle G is strictly inside rectangle H
    if H.rectangle_inside(G):
        print("G is inside H")
    else:
        print("G is not inside H")

    # determine if rectangles G and H overlap (non-zero area of overlap)
    if G.does_intersect(H):
        print("G does overlap H")
    else:
        print("G does not overlap H")

    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle
    newC = C.circle_circumscribes(G)
    print("Circle that circumscribes G: "+ str(newC))

    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle
    newR = G.rect_circumscribe(D)
    print("Rectangle that circumscribes D:" + str(newR))

    # determine if the two rectangles have the same length and width
    if G.__eq__(H):
        print("Rectangle G is equal to H")

    # close the file geom.txt
    file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()