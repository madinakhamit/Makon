import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))
point2 = Point(x2, y2)

print("First point:")
point1.show()

print("Second point:")
point2.show()

print("Distance between points:", point1.dist(point2))

new_x = float(input("Enter new x-coordinate for first point: "))
new_y = float(input("Enter new y-coordinate for first point: "))
point1.move(new_x, new_y)

print("Updated first point:")
point1.show()
